from kivy.uix.screenmanager import ScreenManager
from package.Data import Data
from package.User import User
from package.session import Session

from argon2 import PasswordHasher


class MyScreenManager(ScreenManager):
    def get_gender(self, sex):
        if sex == "Homme":
            return 0
        elif sex == "Femme":
            return 1
        
        
    def check_credentials(self, pseudo:str, password:str):
        print(f"{pseudo} : {password}")
        
        pw = PasswordHasher()
        
        get_user = Data.get_user_with_pseudo(pseudo.lower())
        print(get_user)
        if get_user['status']:
            pass_save = get_user['data']["mot_de_passe"]
            try:
                if pw.verify(pass_save, password):
                    self.current = "index"
                    Session.make_session(get_user)
                return
            except:
                pass
        Session.clear_session()
            
            
    def check_signup(self, username, password:str, password_repeat:str, nameAndSurname, age, sex, taille, poids, travail):
        
        pw = PasswordHasher()
        
        if password != "" and password == password_repeat:
            password = pw.hash(password)
            user = User(username.lower(), password, nameAndSurname, int(age), self.get_gender(sex), int(taille)/100, int(poids), travail)
            data = Data(user)
            status = data.update(True)
            
            if status:
                print("Inscription effectue")
                self.current = "index"
                get_user = Data.get_user(username, password)
                Session.make_session(get_user)
            Session.clear_session()
    
    
    def check_update(self, username, password:str, password_repeat:str, nameAndSurname, age, sexe, taille, weight, work):
        
        old_password = Session.get_session()['data']["mot_de_passe"]
        
        if password  == "" and password_repeat == "":
            password = old_password
        elif password == password_repeat and password != "":
            pw = PasswordHasher()
            password = pw.hash(password)
        else:
            print("Les deux champs de password doivent correspondre")
            return 
            
        user = User(username.lower(),password, nameAndSurname, int(age), self.get_gender(sexe), float(taille)/100, float(weight), work)
        data = Data(user)
        data.update()
        print("mise à jour effectue")
        self.current = "index"
        pass
    
    
    def logout_user(self):
        Session.clear_session()
        self.current = "home"
        pass
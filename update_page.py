from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from package.session import Session

from kivy.properties import StringProperty, NumericProperty, ObjectProperty

Builder.load_file("update_page.kv")

class UpdatePage(BoxLayout):
    username = StringProperty()
    nameAndSurname = StringProperty()
    password = StringProperty()
    age = StringProperty()
    sexe = StringProperty()
    Taille = StringProperty()
    weight = StringProperty()
    work = StringProperty()
    def preload_data(self):
        session = Session.get_session()
        if session['status']:
            data = session['data']
            self.username = data['pseudo'].title()
            self.nameAndSurname = data['nom_prenom']
            self.password = data['mot_de_passe']
            self.age = str(data['age'])
            self.sexe = data['sex'] = "Homme" if data['sex'] == 0 else "Femme"
            self.Taille = str(data['taille']*100)
            self.weight = str(data['poids'])
            self.work = data['travail']
            print(data)
    pass
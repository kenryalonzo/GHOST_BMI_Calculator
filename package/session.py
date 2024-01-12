import json

class Session():
    
    @classmethod
    def make_session(self, data):
        with open('./Data/Session.json', 'w') as file:
            json.dump(data, file)
        
     
    @classmethod   
    def get_session(self):
        with open('./Data/Session.json', 'r') as file:
            data = json.load(file)
            return data
        
        
    @classmethod    
    def clear_session(self):
        data = {"status": False, "data": {"mot_de_passe": "", "pseudo": "", "nom_prenom": "", "age": None, "sex": None, "taille": None, "poids": None, "travail": "", "sante": {'imc':None, 'class_sante':None}}}
        with open('./Data/Session.json', 'w') as file:
            json.dump(data, file)
            

if __name__ == "__main__":
    print(Session.get_session())
    print(Session.clear_session())
class User:
    def __init__(self,pseudo:str, mot_de_passe:str, nom_prenom:str, age:int, sex:int, taille:float, poids:float, travail:str):
        self.mot_de_passe = mot_de_passe
        self.pseudo = pseudo
        self.nom_prenom = nom_prenom
        self.age = age
        self.sex = sex
        self.taille = taille
        self.poids = poids
        self.travail = travail
        pass
    
    def get_data(self):
        return self.__dict__

if __name__ == "__main__":
    user1 = User("rach", 20, 0, 175, 66)
    user2 = User("rach", 20, 0, 175, 66)
    user3 = User("rach", 20, 0, 175, 66)
    print(user1.__dict__)
    print(user2.__dict__)
    print(user3.__dict__)
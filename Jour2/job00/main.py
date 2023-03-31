class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Good morning, my name is {} {}".format(self.prenom, self.nom))


    #"Renvoie une variable contenant le nom et prenom du personnage"
    def get_name(self):
        return(self._nom)

    def get_prenom(self):
        return(self._prenom)


    #"Renvoie une variable permettant de modifier le nom  et prenom du personnage"
    def set_name(self, nom):
        self._nom = nom

    def set_prenom(self, prenom):
        self._prenom = prenom


# Instancier des personnes
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupent", "Marie")
personne3 = Personne("Barka", "Salah")


# On appelle la méthode se présententer 
personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()

# On change le nom et prenom de la 1ere personne
personne1.set_name("lili")
personne1.set_prenom("lili")

print(personne1.get_name())
print(personne1.get_prenom()) 
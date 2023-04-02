class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def getTitre(self):
        print("Nom de l'auteur", self.auteur)

livres1 = Livre("Harry Potter", "elisabethe")
livres2 = Livre("Le seigneur des anneaux", "J.R.R. Tolkien")

livres1.getTitre()



class Personne:
    def __init__(self, nom, prenom):
        self.nom =  nom
        self.prenom = prenom



class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    

    def listerOeuvre(self):
        for livres in self.oeuvre:
            print(livres.titre)

    def ecrireUnLivre(self, titre):
        livres = Livre(titre, self)
        self.oeuvre.append(livres)       

# créer un auteur
auteur1 = Auteur("Dupont", "Pierre")

# ajouter un nouveau livre à l'oeuvre de l'auteur
nouveau_livre = auteur1.ecrireUnLivre("Le Voyage")
nouveau_livre = auteur1.ecrireUnLivre("Les Vagues")

# afficher la liste des livres de l'auteur pour vérifier que le nouveau livre a été ajouté
auteur1.listerOeuvre()





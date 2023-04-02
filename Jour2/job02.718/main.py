class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = {}

    def inventaire(self):
        if not self.collection:
            print("Vous n'avez aucun livre en possession.")
        else:
            print("Vous avez les livres suivants:")
            for livre, quantite in self.collection.items():
                print(f"{quantite} x {livre.titre} de {livre.auteur.nom}.")


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if livre in self.catalogue:
                    self.catalogue[livre] += quantite
                else:
                    self.catalogue[livre] = quantite
                print(f"{quantite}x {titre} de {auteur.nom} ajouté(s) au catalogue de {self.nom}.")
                return 
        print(f"{titre} de {auteur.nom} n'existe pas dans sa collection d'oeuvres.")   


    def inventaire(self):
        if not self.catalogue:
            print(f"{self.nom} n'a aucun livre en stock.")
        else:
            print(f"{self.nom} a les livres suivants en stock:")
            for livre, quantite in self.catalogue.items():
                print(f"{quantite}x {livre.titre} de {livre.auteur.nom}.")


    def rendreLivres(self, client):
        for livre, quantite in client.collection.items():
            if livre in self.catalogue:
                self.catalogue[livre] += quantite
            else:
                self.catalogue[livre] = quantite
                print(f"{quantite}x {livre.titre} de {livre.auteur.nom} rendu(s) à {self.nom}.")

        client.collection = {}
        print(f"Tous les livre ont été rendus à la bibliothèque.")

    def louer(self, client, titre):
        for livre in self.catalogue:
            if livre.titre == titre and self.catalogue[livre] > 0:
                client.collection[livre] = client.collection.get(livre, 0) + 1
                self.catalogue[livre] -= 1
                print(f"{client.nom} a loué le livre '{livre.titre}'. ")
            else:
                print(f"Le livre '{livre}' n'est pas disponible en ce moment")

    # Les clients
    client1 = Client("Alice", "abdou")
    client2 = Client("Lili", "dupent")
    client3 = Client("Marie", "adb")

    catalogue = {
        "Harry Potter et la pierre philosophale": 5,
        "Le seigneur des anneaux": 3,
        "Les misérables": 7,
        "Guerre et paix": 2
    }

    #les livres louer 
    louer(client1, "Harry Potter et la pierre philosophale", catalogue) 
    louer(client1, "Le seigneur des anneaux", catalogue) 

    inventaire(catalogue)

# Instanciation des auteurs
auteur1 = Personne("Hugo", "Victor")
auteur2 = Personne("Shakespeare", "William")

 # Création de la bibliothèque
bibliotheque = Bibliotheque("Ma bibliothèque")

# Livres crèer par les auteurs  auteur, titre, quantite
bibliotheque.acheterLivre(auteur1, "Les Misérables", 1)
bibliotheque.acheterLivre(auteur1, "Notre-Dame de Paris", 3)
bibliotheque.acheterLivre(auteur2, "Hamlet", 8 )

    
   

   

    

   
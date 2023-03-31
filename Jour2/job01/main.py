class Book:
    def __init__(self, title, auteur):
        self.title = title
        self.auteur = auteur
       
    def print(self):
        print(self.title)


class Personne:
    def __init__(self, name, firstname):
        self.name = name
        self.firstname = firstname


class Author(Personne):
    def __init__(self, name, firstname):
        super().__init__(name, firstname)
        self.oeuvre = []


    def listerOeuvre(self):
        print(f"Liste des livres de {self.name} {self.firstname} :")
        for livre in self.oeuvre:
            print("- ", livre.title)


    def ecrireUnLivre(self, title):
        books = Book(title, self)
        self.oeuvre.append(books)

        return books
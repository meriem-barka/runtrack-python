class Personne:
    def __init__(self, name, firstname):
        self.name = name
        self.firstname = firstname

class Client(Personne):
    def __init__(self, name, firstname):
        super().__init__(name, firstname)


class Bibliotheque:
    def __init__(self, name):
        self.name = name
        self.catalogue = {}


from random import random

class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def grille_vide():
        return[[0] * 7 for i in range(6)]
    print(grille_vide())

print(random())
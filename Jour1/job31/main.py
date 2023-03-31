import re 

while True:
    word = input("Enter a word without spaces, accents or capitals: ")
    if re.match("^[a-z]+$", word):
        print("Word is valid:", word)
        break
    else:
        print("The word must contain only letters of the alphabet without spaces, accents or capitals.", word)

# Convertit le mot en une liste de lettres
list_letter = sorted(word)

# Trie les lettres dans l'ordre alphabétique
lettres_triees = sorted(list_letter )



mot = input("Entrez un mot sans espace, accent ou majuscule : ")

# Convertit le mot en une liste de lettres
lettres = list(mot)

# Trie les lettres dans l'ordre alphabétique
lettres_triees = sorted(lettres)

# Compare le mot d'origine avec la version triée des lettres
if lettres_triees == lettres:
    print("Le mot", mot, "est déjà le plus grand mot dans l'ordre alphabétique.")
else:
    # Recherche la première lettre dans le mot qui peut être remplacée par une lettre plus grande
    for i in range(len(lettres)-1, 0, -1):
        if lettres[i] > lettres[i-1]:
            # Trouve la plus petite lettre dans le suffixe à droite de la lettre à changer
            j = i
            while j < len(lettres) and lettres[j] > lettres[i-1]:
                j += 1
            # Echange les lettres
            lettres[i-1], lettres[j-1] = lettres[j-1], lettres[i-1]
            # Trie le suffixe à droite de la lettre changée
            lettres[i:] = sorted(lettres[i:])
            break
    # Affiche le nouveau mot
    print("Le mot modifié est :", "".join(lettres))

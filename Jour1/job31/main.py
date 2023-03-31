import re 

while True:
    word = input("Enter a word without spaces, accents or capitals: ")
    if re.match("^[a-z]+$", word):
        print("Word is valid:", word)
        break
    else:
        print("The word must contain only letters of the alphabet without spaces, accents or capitals.", word)

# Convertit le mot en une liste de lettres
list_letter = list(word)

# Trie les lettres dans l'ordre alphabétique
lettres_triees = sorted(list_letter)

# Compare le mot d'origine avec la version triée des lettres
if lettres_triees == list_letter:
    print("word", word)
else:
    # Recherche la première lettre dans le mot qui peut être remplacée par une lettre plus grande
    for i in range(len(list_letter)-1, 0, -1):
        if list_letter[i] > list_letter[i-1]:
            # Trouve la plus petite lettre dans le suffixe à droite de la lettre à changer
            j = i
            while j < len(list_letter) and list_letter[j] > list_letter[i-1]:
                j += 1
            # Echange les list_letter
            list_letter[i-1], list_letter[j-1] = list_letter[j-1], list_letter[i-1]
            # Trie le suffixe à droite de la lettre changée
            list_letter[i:] = sorted(list_letter[i:])
            break
    # Affiche le nouveau mot
    print("Le mot modifié est :", "".join(list_letter))

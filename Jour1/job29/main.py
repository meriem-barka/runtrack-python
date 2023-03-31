def list_notes(notes):
    # Arrondit les notes des étudiants
    notes_arrondies = []
    for note in notes:
        if note < 40:
            print("l'étudiant a échoué, pas d'arrondi")
            notes_arrondies.append(note)
        elif note % 5 > 2:
            print("l'étudiant a réussi et sa note doit être arrondie")
            notes_arrondies.append(note + (5 - note % 5))
        else:
            print("l'étudiant a réussi, mais sa note ne doit pas être arrondie")
            notes_arrondies.append(note)
    return notes_arrondies

    # Exemple d'utilisation avec une liste de notes d'étudiants
notes = [82, 75, 68, 91, 45, 57, 89, 38]
notes_arrondies = list_notes(notes)
print(notes_arrondies)


text = input("Veiller renseigner une chaîne de caractères: ")

with open("Output.txt", "w") as text_file:
    text_file = open("Output.txt", "w")
    text_file.write(text)
    text_file.close()
def draw_triangle(height):
     # Dessiner un triangle
    for i in range(height):
        # Affiche la partie supérieure du triangle
        for j in range(height - i - 1):
            print(" ", end="")
        print("/", end="")
        for j in range(i * 2):
            if i == height - 1:
                print("_", end="")
            else:
                print(" ", end="")
        print("\\", end="")
        print("")
    

# Exemple d'utilisation avec une hauteur de 5
draw_triangle(5)




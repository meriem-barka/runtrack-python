def draw_rectangle(width, height):
    # Dessiner un rectangle
    for i in range(height):
        print("|", end="")
        for j in range(width):
          if(i== 0 or i == height-1):
            print("-",end='')
          else:
            print(" ", end='')
        print("|")


# Test du programme avec un rectangle de dimensions (10, 3)
draw_rectangle(10, 3)

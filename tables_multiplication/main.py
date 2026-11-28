def afficher_table_multiplication(n, min = 1, max = 10):
    print()
    if min > max:
        print("ERREUR : Le max doit être plus grand ou égal au min")
        return

    for i in range(min, max + 1): # Note: min est inclusif et max est exclusif, c'est pour ça le + 1
        print(i, "x", n, "= ", i * n)
    print("---------- Fin ----------")

afficher_table_multiplication(6)  
afficher_table_multiplication(5, 20, 12) 
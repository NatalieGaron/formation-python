import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_VIES = 4

def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Veuillez saisir un nombre entre {nb_min} et {nb_max}: ")
        try:
            nombre_int = int(nombre_str)
        except ValueError:
            print("Vous devez saisir un nombre entier.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Le nombre saisi {nombre_int} n'est pas compris entre {nb_min} et {nb_max}.")
                nombre_int = 0
    return nombre_int

""" 
nombre = 0
vies = NOMBRE_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies.")

    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print(f"Bravo! T'as gagné")
    elif nombre < NOMBRE_MAGIQUE:
        print(f"Le nombre saisi {nombre} est inférieur au nombre magique.")
        vies -= 1
    else:
        print(f"Le nombre saisi {nombre} est supérieur au nombre magique.")
        vies -= 1
if vies == 0:
    print(f"Vous avec perdu, le nombre était {NOMBRE_MAGIQUE}.")
"""

gagne = False
for i in range(0, NOMBRE_VIES):
    vies = NOMBRE_VIES - i;
    print(f"Il vous reste {vies} vies.")

    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print(f"Bravo! T'as gagné")
        gagne = True
        break
    elif nombre < NOMBRE_MAGIQUE:
        print(f"Le nombre saisi {nombre} est inférieur au nombre magique.")
    else:
        print(f"Le nombre saisi {nombre} est supérieur au nombre magique.")

if not gagne:
    print(f"Vous avec perdu, le nombre était {NOMBRE_MAGIQUE}.")
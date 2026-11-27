import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_QUESTIONS = 4

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1) # 0 -> +, 1 -> *  
    
    operateur_str = "+"
    if o == 1:
        operateur_str = '*'

    reponse_str = input(f"Calculez {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)

    calcul = a + b
    if o == 1:
        calcul = a * b

    if reponse_int == calcul:
        return True
  
    return False

nb_points = 0
for i in range(0, NOMBRE_QUESTIONS):
    print(f"Question {i + 1} sur {NOMBRE_QUESTIONS}:")
    if poser_question():
        nb_points += 1
        print(f"Réponse correcte")
    else:
        print(f"Réponse incorrecte")
    print()

print(f"Vous avez {nb_points} points sur {NOMBRE_QUESTIONS}")
moyenne = int(NOMBRE_QUESTIONS / 2)  # va prendre le nombre avant le point
if nb_points == NOMBRE_QUESTIONS:
    print("Y'a rien-là mais bravo")
elif nb_points == 0:
    print("T'es poche")
elif nb_points > moyenne:
    print("T'es correct")
else:
    print("T'es un peu poche")
""" 
Dans la formation ce ficher est dans un projet dans un répertoire appellé programme-tortue 
et le fichier s'appelle main.py
"""

import turtle

t = turtle.Turtle()

# ----------------------------------
# 5 marches de 30 pixels
# ----------------------------------

""" 
# marche 1
t.forward(30)

# marche 2
t.left(90)
t.forward(30)
t.right(90)
t.forward(30)

# marche 3
t.left(90)
t.forward(30)
t.right(90)
t.forward(30)

# marche 4
t.left(90)
t.forward(30)
t.right(90)
t.forward(30)

# marche 5
t.left(90)
t.forward(30)
t.right(90)
t.forward(30)
"""

def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)

# escalier(30, 5)

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

# carre(30)
# carre(100)

def carres(taille_depart, nb):
    for i in range(0, nb):
        taille = (i + 1) * taille_depart  
        carre(taille)

carres(30, 5)    

turtle.done()
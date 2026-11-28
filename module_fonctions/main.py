"""
nom = "toto"
print("Je m'appelle " + nom) # Je m'appelle toto
# Dans le code suivant print fais la conversion et ajoute un espace avant de concaténer
print("Je m'appelle", nom, "et j'ai", 30, "ans")  # Je m'appelle toto et j'ai 30 ans
"""

""" 
nom = input("Votre nom? ") # Retourne le nom, fonction bloquante
print("Votre nom est " + nom)
"""

# *Note, en Python, les fonction doivent être définie avant les appels dans un fichier

# Le return sert à:
#    sortir d'un fonction 
#    retourner une valeur (facultatif)
# Le return n'est pas obligatoire
# C'est une mauvaise pratique de mettre un return inutile à la
# toute fin d'une fonction si on a rien à retourner
# C'est une mauvaise pratique d'avoir des return qui retournent une 
# valeur et des return qui n'en retournent pas dans la même fonction

"""
def afficher_infos_personne(nom="", age = -1):
    if nom == "":
        print("Vous n'avez pas passé de nom.")
        print()
        return
    
    if age == -1:
        print("La personne s'appelle", nom + ".")
    else:
        print("La personne s'appelle", nom + ", son âge est de", age, "ans.")
    
    print("Son nom comporte", len(nom), "caractères.")
    print()
"""

"""
afficher_infos_personne("Cappucc", 10)
afficher_infos_personne("Patate")
afficher_infos_personne(age=28)
afficher_infos_personne()
"""

# Dans le programme principal, on ne peut pas utiliser
# return pour sortir du programme principal mais on peut 
# utiliser exit(), on peut mettre un code dans le paramètre

def est_majeur(age: int) -> bool: # On spécifie le type de cette façon mais c'est facultatif dans la plupart des cas
    if age >= 18:
        return True
    return False

def recuperer_infos_personne(numero_personne):
    nom_personne = input(f"Nom de la personne " + str(numero_personne) + ":")
    age_personne = input(f"Age de la personne " + str(numero_personne) + ":")
    return nom_personne, int(age_personne)

def afficher_infos_personne(numero_personne, nom, age: int):
    print("La personne", numero_personne, "est", nom +", son age est", str(age) + ".")
    print("Le nom comporte ", len(nom), "caractères.")
    if est_majeur(age):
        print("Il est majeur")
    else:
        print("Il est mineur")

def recuperer_et_afficher_infos_personne(numero_personne):
    nom, age = recuperer_infos_personne(numero_personne)
    afficher_infos_personne(numero_personne, nom, age)

nb_personnes = 3
for i in range(nb_personnes): # 0 1 2
    recuperer_et_afficher_infos_personne(i + 1)


    
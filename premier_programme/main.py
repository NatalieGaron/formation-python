# Commentaire sur une ligne

""" Premier programme 
Formation Python
apprendre la programmation en Python """

def afficher_information_personne(nom, age, taille = 0): # taille = 0 est un paramètre optionnel
  print()
  
  print('Vous vous appelez ' + nom + ', vous avez ' + str(age) + ' ans.')
  print(f"Vous vous appelez {nom}, vous avez {age} ans.")
  print("Vous vous appelez %s, vous avez %s ans." % (nom, age))
  
  print('L\'année prochaine, vous aurez ' + str(age + 1) + ' ans.') 
  print("L'année prochaine, vous aurez %s ans." % (age + 1)) 
  
  if age == 17:
    print('Vous êtes presque majeur.')  
  elif 12 <= age < 18:  # age >= 12 and age < 18:
    print('Vous êtes adolescent.')  
  elif age == 1 or age == 2:
    print('Vous êtes un bébé.')
  elif age == 18:
    print('Tout juste majeur : félicitations')
  elif age > 60:
    print('Vous êtes un senior.')
  elif age < 10:
    print('Vous êtes un enfant.')
  elif age > 18:
    print('Vous êtes majeur.')  
  else:
    print('Vous êtes mineur.')

  # Afficher la taille
  if taille != 0: # if not taille == 0:
    print('Votre taille est de ' + str(taille) + ' m.') 

def demander_nom():
  reponse_nom = ""
  while reponse_nom == "":
    reponse_nom = input("Quel est votre nom ? ")
  return reponse_nom

def demander_age(nom_personne):
  age_int = 0
  while age_int == 0:
    try:
      age_int = int(input(nom_personne + ", quel est votre age ? "))
    except ValueError:
      print("ERREUR: L'âge doit être un nombre entier.")
  return age_int

# -----------------------------------------------------------------------

# Pour comprendre comment fonctionne le keyword global
# Dès que tu réaffectes (fais un = sur) une variable globale à l'intérieur d'une fonction, tu dois utiliser 
# le keyword global mais ce n'est pas nécessaire si on ne fait que la lire.
# Par contre, si la variable contient un objet modifiable (liste, dictionnaire, etc.) et que tu modifies 
# l'objet sans faire de réaffectation, global n'est pas nécessaire
# ex.  noms = ["Alice", "Bob"]
#      def ajouter_nom():
#        noms.append("Charlie")
""" 
age = 0

def demander_Age():
  global age
  while age == 0:
    try:
      age = int(input("Quel est votre age ? "))
    except ValueError:
      print("ERREUR: L'âge doit être un nombre entier.")

demander_Age()
""" 

""" 
nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

afficher_information_personne(nom1, age1)
afficher_information_personne(nom2, age2)
"""

# Afficher la taille
"""
taille = 1.75 # float
print(type(taille)) 
print("Votre taille est de " + str(taille) + " m.")
"""

# Boucle for
# Paramètres : range(start, stop, step) 
"""
for i in range(4, 8, 2):
  print("i = " + str(i))  
"""

NB_PERSONNES = 3  # En Python, les constantes sont en majuscules par convention
                  # Ce ne sont pas de vraies constantes, elles peuvent être modifiées mais c'est déconseillé.
for i in range(0, NB_PERSONNES):
  nom = "Personne-" + str(i)
  age = demander_age(nom)
  if i == 0:
    afficher_information_personne(nom, age)
  else:
    afficher_information_personne(nom, age, 1.75) 

print()
print("""
   On arrange ça comme
       on veut, mais il faut faire attention 
             aux indentations.
""")
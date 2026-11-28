def poser_question(question, choix_a, choix_b, choix_c, choix_d, reponse_correcte):
    global score

    print("Question:", question)
    print("(a)", choix_a)
    print("(b)", choix_b)
    print("(c)", choix_c)
    print("(d)", choix_d)

    ret = False
    choix_user = input("Votre réponse: ")
    if choix_user == reponse_correcte:
        score += 1
        ret = True
        print("C'est beau")
    else:
        print("C'est pas ça")
    print()
    

score = 0
poser_question("Quelle est la capitale de la France?", "Marseille", "Nice", "Paris", "Nantes", "c")
poser_question("Quelle est la capitale de l'Italie?", "Rome", "Venise", "Pise", "Florence", "a")
print(f"Votre score: {score}") 

def Joueur1():
    while True:
        try:
            a = int(input("joueur 1 entrer une case :"))
            if p[a] == " ":
                p[a] = "X"
                break
            else:
                print("entrer un nombre valide :")
        except:
            print("vous n'avez pas écrit sous la forme demandée")

def Joueur2():
    while True:
        try:
            a = int(input("joueur 2 entrer une case :"))
            if p[a] == " ":
                p[a] = "O"
                break
            else:
                print("entrer un nombre valide :")
        except:
            print("vous n'avez pas écrit sous la forme demandée")

def afficherJeu():
    print("\n\n " +p[1]+" |"+" "+p[2]+" |"+" "+p[3])
    print("---+---+---")
    print(" "+p[4]+" |"+" "+p[5]+" |"+" "+p[6])
    print("---+---+---")
    print(" "+p[7]+" |"+" "+p[8]+" |"+" "+p[9]+"\n\n")

def verification(joueurQuiJoue):
    global gagnant
    if p[1] == p[2] and p[2] == p[3] and p[1] != " ":
        print("Le {0} a gagné\n\n".format(joueurQuiJoue))
        gagnant = True
    elif p[4] == p[5] and p[5] == p[6] and p[4] != " ":
        print("Le {0} a gagné\n\n".format(joueurQuiJoue))
        gagnant = True
    elif p[7] == p[8] and p[8] == p[9] and p[7] != " ":
        print("Le{0} a gagné\n\n".format(joueurQuiJoue))
        gagnant = True
    elif p[1] == p[4] and p[4] == p[7] and p[1] != " ":
        print("Le {0} a gagné\n\n".format(joueurQuiJoue))
        gagnant = True
    elif p[2] == p[5] and p[5] == p[8] and p[2] != " ":
        print("Le {0} a gagné\n\n".format(joueurQuiJoue))
        gagnant = True
    elif p[3] == p[6] and p[6] == p[9] and p[3] != " ":
        print("Le {0} a gagné\n\n".format(joueurQuiJoue))
        gagnant = True
    elif p[1] == p[5] and p[5] == p[9] and p[1] != " ":
        print("Le {0} a gagné\n\n".format(joueurQuiJoue))
        gagnant = True
    elif p[7] == p[5] and p[5] == p[3] and p[7] != " ":
        print("Le {0} a gagné\n\n".format(joueurQuiJoue))
        gagnant = True

while True:
    p = []
    gagnant = False
    a = 1
    
    for i in range(0,10):
        p.append(" ")
    p[0] = "a"
    if a == 1:
        while True:
            Joueur1()
            afficherJeu()

            verification("joueur 1")
            if gagnant:
                a = 2
                break
            if p.count(" ") == 0 and gagnant == False:
                print("personne n'a gagné\n\n")
                break
            Joueur2()
            afficherJeu()

            verification("joueur 2")
            if gagnant:
                a = 1
                break
            if p.count(" ") == 0 and gagnant == False:
                print("personne n'a gagné\n\n")
                break

    p = []      
    gagnant = False
    for i in range(0,10):
        p.append(" ")
    p[0] = "a"

    if a == 2:
        while True:
            Joueur2()
            afficherJeu()

            verification("joueur 2")
            if gagnant:
                a = 1
                break

            Joueur1()
            afficherJeu()

            verification("joueur 1")
            if gagnant:
                a = 2
                break

    
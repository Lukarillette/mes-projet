continuer = True
while continuer:
    nombre = int(input("Quel est le nombre? "))
    diviseur = 2

    print("facteur premier de" ,nombre ,"est")
    while diviseur<=nombre:
        if nombre%diviseur == 0 :
            nombre=nombre/diviseur
            print(nombre ,"  " ,diviseur)
        else:
            diviseur = diviseur +1

    choix = input("si vous voulez continuer taper + sinon une autre touche")
    if choix not in ('+'):
        continuer = False

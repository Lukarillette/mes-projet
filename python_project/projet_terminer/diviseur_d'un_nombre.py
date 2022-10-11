continuer = True
while continuer:
    nombre = int(input("quelle est le nombre"))
    diviseur = 1
    print("les diviseur de" ,nombre ,"sont" )
    while diviseur <= pow(nombre,0.5):
        if nombre%diviseur == 0:
            print(diviseur)
            diviseur = diviseur + 1
        else:
            diviseur = diviseur + 1

    choix = input("Voulez vous continuer ? ")
    if choix not in ('+'):
        continuer = False

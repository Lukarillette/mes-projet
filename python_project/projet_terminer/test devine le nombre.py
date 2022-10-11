from random import randint
continuer = True
nombre_a_deviner = randint(1,50)
essai = 1 
while continuer:
    essai_reponse = int(input("quelle est votre nombre ?"))
    if nombre_a_deviner == essai_reponse:
        continuer = False
        print("bravo vous avez mis",essai,"essais avant de trouver le bon résultat")
    else:
        if nombre_a_deviner > essai_reponse:
            print("le nombre à trouver est supérieur")
            essai = essai + 1
        else:
            print("le nombre à trouver est inféieur")
            essai = essai + 1
        if essai == 15:
            continuer = False
            print("vous avez perdu car vous avez mis plus de 10 essais")




from operator import truediv


def hypotenuse_inconnu(a,b): 
    return pow((a*a+b*b),0.5)

def hypotenuse_connu(a,b):
    if a>b:
        return pow((a*a-b*b),0.5)
    else:
        return pow((b*b-a*a),0.5)

def verification_rectange(a,b,c):
    d = max(a,b,c)
    d = d*d
    ab = a*a+b*b
    return "a + b = {0} \nd = {1}".format(ab,d)

continuer = True
while continuer:
    choix = int(input("pythagore =  1\nrectangle ? = 2\n"))
    if choix == 1:
        choix_1 = int(input("hypoténuse connu = 1\nhypoténuse inconnu= 2\n"))
        if choix_1 == 1:
            a = float(input("entrer les nombres\n"))
            b = float(input())
            print(hypotenuse_connu(a,b))
        else:
            a = float(input("entrer les nombres\n"))
            b = float(input())
            print("\n")
            print(hypotenuse_inconnu(a,b))
    else:
        print("veuillez entrer les nombres sous la forme :")
        a = input("adjacent ")
        a = float(a)
        b = input("adjacent ")
        b = float(b)
        c = input("hypotenuse ")
        c = float(c)
        print("\n")
        print(verification_rectange(a,b,c))
        print("\n")
        reponse = input("voulez-vous continuer ?\n+ = oui\n- = non")  

if reponse == "+":
    continuer = True
else:
    continuer = False

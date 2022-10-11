#from multiprocessing.sharedctypes import Value
#from tkinter import N
def diviseur(a,b):
    d = 1
    for i in range(1,a+1):
        if a%d == 0:
            liste_diviseur_1.append(d,)
            d=d+1
        else:
            d=d+1
    d=1
    for i in range(1,b+1):
        if b%d == 0:
            liste_diviseur_1.append(d,)
            d=d+1
        else:
            d=d+1
liste_diviseur_1 = []

a = int(input("nombre 1 =>"))
b = int(input("nombre 2 =>"))
diviseur(a,b)

liste_diviseur_1.sort()
m = liste_diviseur_1.count(max(liste_diviseur_1))
while m == 1:
    liste_diviseur_1.pop()
    m = liste_diviseur_1.count(max(liste_diviseur_1))

z = max(liste_diviseur_1)
print("le diviseur commun est {0} voici les résultat:\n\n{1} = {2}\n{3} = {4}\n".format(z,a,a/z,b,b/z))
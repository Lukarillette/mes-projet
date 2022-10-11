continuer = "+"
while continuer == "+":
    nombre = int(input("quelle est le nombre dont \n tu veux connaitre la table ?"))
    for i in range(1,11):
        print("{0} * {1} = {2}".format(i,nombre,nombre*i))
    continuer = input("voulez vous recommencer +/- ?")
print("fin")
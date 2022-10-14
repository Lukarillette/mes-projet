def reunion_intersection():
    a = int((input("entrer l'intervalle => ")))
    b = int((input()))
    intervalle_1 = list(range(a,b+1))
    c = int(input("entrer l'intervalle => "))
    d = int(input())
    intervalle_2 = list(range(c,d+1))
    reponse_intersection = sorted(list(set(intervalle_1)&set(intervalle_2)))
    n = len(reponse_intersection)
    for i in range(1,n-1):
        e = 1
        reponse_intersection.pop(e)
        e = e + 1
    reponse_reunion = sorted(list(set(intervalle_1)|set(intervalle_2)))
    compteur = len(reponse_reunion)
    for i in range(1,compteur-1):
        e = 1
        reponse_reunion.pop(e)
        e = e + 1
    n = len(intervalle_1)
    for i in range(1,n-1):
        e = 1
        intervalle_1.pop(e)
        e = e + 1
        n = len(intervalle_2)
    for i in range(1,n-1):
        e = 1
        intervalle_2.pop(e)
        e = e + 1
    if not reponse_intersection:
        reponse_intersection = "il n'y a pas d'intersections"
    print("-------------\nI = {0}       J = {3}\nintersection : {1}\nreunion : {2}\n-------------".format(intervalle_1,reponse_intersection,reponse_reunion,intervalle_2))
continuer = "oui"
while continuer == "oui":
    reunion_intersection()

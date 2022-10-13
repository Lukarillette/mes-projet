def intersection():
    print("----------\nintersection\n----------")
    a = int(input("entrer l'intervalle => "))
    b = int(input())
    intervalle_1 = list(range(a,b+1))
    c = int(input("entrer l'intervalle => "))
    d = int(input())
    intervalle_2 = list(range(c,d+1))    
    reponse = list(set(intervalle_1)&set(intervalle_2))
    n = len(reponse)
    for i in range(1,n-1):
        e = 1
        reponse.pop(e)
        e = e + 1
    if not reponse:
        print("-------------\nil n'y a pas d'intersections")
    else:
        print("-------------\n",reponse)

def reunion():
    print("----------\nreunion\n----------")
    a = int(input("entrer l'intervalle => "))
    b = int(input())
    intervalle_1 = list(range(a,b+1))
    c = int(input("entrer l'intervalle => "))
    d = int(input())
    intervalle_2 = list(range(c,d+1))
    reponse = sorted(list(set(intervalle_1)|set(intervalle_2)))
    n = len(reponse)
    for i in range(1,n-1):
        e = 1
        reponse.pop(e)
        e = e + 1
    if not reponse:
        print("-------------\nil n'y a pas de reunion")
    else:
        print("-------------\n",sorted(reponse))

choix = int(input("intersection = 1\nreunion = 2\n"))
if choix == 1:
    continuer = "oui"
    while continuer == "oui":
        intersection()
        z = input("-------------\ncontinuer ? + = oui,- = non")
        if z == "-":
            continuer = "non"
elif choix == 2:
    continuer = "oui"
    while continuer == "oui":
        reunion()
        z = input("-------------\ncontinuer ? + = oui,- = non")
        if z == "-":
            continuer = "non"



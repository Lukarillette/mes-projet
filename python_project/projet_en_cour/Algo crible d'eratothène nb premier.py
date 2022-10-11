from math import*

def EstPremier(N):
    if N <= 0:
        return("Le nombre est négatif, donc non premier")
    if N == 1: # Cas du nombre 1 :
        return("Le Nombre",N,"est un cas particulier")
    p = 2
    while p <= sqrt(N):
        reste = N%p  #reste de la division euclidienne :
        if reste == 0:
            return("Le nombre ",N," n'est donc pas premier")
        p = p+1
    return("Le nombre",N," est donc premier")
    
liste_nombre_premier = []
# vous pouvez modifier la valeur de l'entier N  nombre d'entier naturel souhaité:
N = int(input("Entrer votre nombre"))
for i in range(1,N+1):
    print(EstPremier(i))


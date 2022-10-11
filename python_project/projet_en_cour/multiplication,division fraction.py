from unittest import result


def division_fractions(a,b,c,d):
    resultat_1 = a*d
    resultat_2 = b*c
    return resultat_1,resultat_2

def multiplication_fractions(a,b,c,d):
    resultat_1 = a*c
    resultat_2 = b*d
    return resultat_1,resultat_2


rep = input("veut tu diviser ou multiplier")
if rep == "×":
    a = int(input("taper les nombres sous la forme a b c d"))
    b = int(input())
    c = int(input())
    d = int(input())
    print(multiplication_fractions(a,b,c,d))
else:
    a = int(input("taper les nombres sous la forme a b c d"))
    b = int(input())
    c = int(input())
    d = int(input())
    print(division_fractions(a,b,c,d))

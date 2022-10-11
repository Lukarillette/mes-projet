def masse_volumique(a,b):
    return a/b
reponse = int(input("masse volumique = 1\nmasse = 2\nvolume = 3\ndensité = 4\nvolumique/massique = 5\n"))
if reponse == 1:
    masse_ = float(input("la masse => "))
    volume = float(input("le volume => "))
    print(masse_volumique(masse_,volume))
elif reponse == 2:
    m_vol = float(input("la masse volumique => "))
    volume = float(input("le volume => "))
    print(m_vol*volume)
elif reponse == 3:
    masse_ = float(input("la masse =>"))
    m_vol = float(input("la masse volumique => "))
    print(masse_volumique(masse_,m_vol))
elif reponse == 4:
    m_vol = float(input("la masse volumique => "))
    print("la densité est", m_vol/1)
elif reponse == 5:
    print("x en %     masse ou volume de l'éspèce\n______     ___________________________\n 100          volume ou masse total")

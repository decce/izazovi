import random

#nivo1.
#coin = ["g", "p"]
#unos = input("Glava ili pismo? Uneti g za glavu, p za pismo: ")
#rcoin = random.choice(coin)
#for i in coin:
#    if i != unos:
#        print("Došlo je do greške!")
#        quit()
#    elif unos == rcoin:
#        print("Tačno!")
#        quit()
#    elif unos != rcoin and (unos == coin[0] or unos == coin[1]):
#        print("Netačno!")
#        quit()

#nivo2.
while True:
    broj1 = random.randint(0, 1001)
    print(broj1)
    unos = input("Da li ce sledeci broj biti visi ili nizi?: ")
    broj2 = random.randint(0, 1001)

    if unos == "visi" and broj2 > broj1:
        print("Tacno! Drugi broj je bio", broj2, "\n")
    elif unos == "visi" and broj2 < broj1:
        print("Netacno! Drugi broj je bio", broj2, "\n")
    elif unos == "nizi" and broj2 > broj1:
        print("Netacno! Drugi broj je bio", broj2, "\n")
    elif unos == "nizi" and broj2 < broj1:
        print("Tacno! Drugi broj je bio", broj2, "\n")
    else:
        print("Doslo je do greske. \n")

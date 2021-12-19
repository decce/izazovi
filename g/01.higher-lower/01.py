import random

#nivo1.
coin = ["g", "p"]
unos = input("Glava ili pismo? Uneti g za glavu, p za pismo: ")
rcoin = random.choice(coin)
for i in coin:
    if i != unos:
        print("Došlo je do greške!")
        quit()
    elif unos == rcoin:
        print("Tačno!")
        quit()
    elif unos != rcoin and (unos == coin[0] or unos == coin[1]):
        print("Netačno!")
        quit()


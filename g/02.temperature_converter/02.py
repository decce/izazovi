#nivo1.
#f = input("Uneti temperaturu u farenhajtima: ")
#c = (int(f) - 32) * (5/9)
#print("Uneta temperatura u celzijusima je", c)

#nivo2.
k = input("Izabrati pocetni sistem, uneti f za farenhajt, c celzijus: ")
temp = input("Uneti brojnu vrednost: ")
if k == "f":
    c = (int(temp) - 32) * (5/9)
    print("Temperatura u celzijusu je:", c)
elif k == "c":
    f = (int(temp) * (5/9)) + 32
    print("Temperatura u farenhajtu je:", f)
else:
    print("Doslo je do greske.")

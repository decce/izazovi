import names
import random
import datetime

#nivo1.
ime = input("Izaberite pol, m za muški, f za ženski: ")
if ime == "m":
    print("\n  ",names.get_full_name(gender='male'))
elif ime == "f":
    print("\n  ",names.get_full_name(gender='female'))
else:
    print("Došlo je do greške.")
    quit()

#nivo2.
print("Fizičke karakteristike:")
krv = ["A+","A-","B+","B-","AB+","AB-","O+","O-"] 
print(" Visina:", random.randrange(130, 220), "cm")
print(" Težina:", random.randrange(50, 150), "Kg")
print(" Krvna grupa:", random.choice(krv))

#nivo3.


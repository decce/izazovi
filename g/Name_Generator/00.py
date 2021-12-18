import names
import random

#nivo1.
print(names.get_full_name())

#nivo2.
a = ["A+","A-","B+","B-","AB+","AB-","O+","O-"] 
print("Visina:", random.randrange(130, 220), "cm")
print("Težina:", random.randrange(50, 150), "Kg")
print("Krvna grupa:", random.choice(a))


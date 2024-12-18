# Jörn Markus Toomingas 18.12.24
# Kontrolltöö
import random

#1. Korrutamise kontrollimine Jörn Markus Toomingas 18.12.24
"""
a, b = random.randint(1,10), random.randint(1,10),
vastus = int(input(f"Lisa vastus {a}*{b}="))
if vastus == a*b:
    print("Õige")
else:
    print("Vale")
"""
#6. Paaris või paaritu Jörn Markus Toomingas 18.12.24

arv = int(input("Sisesta number: "))
if arv ==0:
    print("Number ei saa olla 0!")
elif (arv%2) == 0:
    print("Arv on paaris")
else:
    print("Arv on paaritu")

#7. Eurokalkulaator Jörn Markus Toomingas 18.12.24
"""
EEK = 15.6466
EUR = 1

Kysimus = int(input("Kui palju raha on? (EUR): "))
if ValueError:
    print("Palun sisestage number.")

Vastus = Kysimus*EEK 

print(Vastus)
"""
#8. Täringud Jörn Markus Toomingas 18.12.24
"""
a = int(input("Tahad mängida? (Ei/Jah)"))
if a=="Jah":
    print("Sa veeretasid", random.randint(1,6))
    if a=="Ei":
        break

"""
#16. Täringud Jörn Markus Toomingas 18.12.24
"""
a = int(input("Tahad mängida? (Ei/Jah)"))
if a=="Jah":
    print("Sa veeretasid", random.randint(1,6))
    if a=="Ei":
        break
"""
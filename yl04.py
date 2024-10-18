#16.10.24 Toomingas
#Ülesanded 04
import turtle

#5. Ringi pindala ja Turtle
try:
    r = int(input("Lisa ringi raadius:  "))
    pi = 3.14
    S = pi * r**2  #Astendamine
    P = 2*pi*r
    print(f"Ringi pindala on {S:.2f} ja ümbermõõt on {P:.2f}")
    turtle.circle(r, 360)
except:
    print("Tegid ssestamisel vea!")

turtle.done


#4. Kingituste pakkimine
try:
    kingitused = int(input("Lisa kingituste arv:  "))
    maht = 5
    pakid = kingitused // maht
    yle = kingitused % maht
    print(f"Saad teha {pakid} täis kinkekasti. Üle jääb {yle} kingitust:  ")
except: 
    print("Tegid sisestamisel vea!")


#3. Faili allalaadimine
try: 
    failisuurus = int(input("Sisesta faili suurus (MB): "))
    downkiirus = int(input("Sisesta allalaadimisekiirus (MB/s): "))
    aeg = failisuurus / downkiirus
    print(f"Allalaadimiseks kulub {aeg:0.2f} sekundit")
except:
    print("Tegid sisestamisel vea!")


#2. Raamatute allahindlus
ale = 0.3
kogus = 3
hind = 12.53
summa = hind - (hind * ale) * kogus
print(f"{kogus} raamatu hind soodustustega on {summa: 0.2f}€")


#1. Aita pikkus
a = int(input("Sisesta külg 1 "))
b = int(input("Sisesta külg 2 "))
P = 2 * (a+b)
print(f"Aia kogupikkus on {P} meetrit.")
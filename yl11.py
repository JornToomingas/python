#08.11.24 Toomingas
#Ülesanne 11
import turtle
import random

#1. Kirjuta funktsioon pikim_sona(), mis võtab sisendiks sõnade listi ja tagastab pikima sõna pikkuse. Prindi tulemus konsooliaknasse.
"""
def pikim_sona(*sonad):
    pikim = 0
    for i in sonad:
        if len(i)>pikim:
            pikim=len(i)
    print(f"Pikim sõna on {pikim} märki!")


pikim_sona("Üks", "Kaks", "Kolmkümmend", "abc123def456ghi789j0")
"""



#2. Kirjuta funktsioon nimega kolm_pikimat_sona(), mis analüüsib sõnade listi ja leiab kolm kõige pikemat sõna. Lisa kontroll juhuks, kui sõnade arv pole piisav.
"""
def kolm_pikimat_sona(a):
    sonastik = {}
    for i in a:
        sonastik[i] = len(i)
    sorteeritud = sorted(sonastik.items(), key=lambda x:x[1], reverse=True)
    for j in range(3):
        print(sorteeritud[j][0])

sonad = ["üks", "kaks", "viis", "kolmsada", "üksmiljonsadamust"]

kolm_pikimat_sona(sonad)
"""






# 3. Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
"""
def sarnased_esitahed(nimi):
    tykk = nimi.split(" ")
    if tykk[0][0] == tykk[1][0]:
        return True
    else:
        return False


print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False
"""

# Kilpkonn – kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.

def viisnurk(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400, 400),random.randint(-400, 400))
        turtle.pendown
        turtle.rt(random.randint(0, 90))
        for i in range(5):
            turtle.fd(100)
            turtle.lt(144)

def ring(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400, 400),random.randint(-400, 400))
        turtle.pendown
        turtle.rt(random.randint(0, 90))
        turtle.circle(360)



def ruut(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400, 400),random.randint(-400, 400))
        turtle.pendown
        turtle.rt(random.randint(0, 90))
        for i in range(4):
            turtle.fd(100)
            turtle.lt(90)

def suvaline():
    for i in range(k):
        random.choice([viisnurk(1), ring(1), ruut(1)])




valik = int(input("1 - viisnurk\n2 - ring\n3 - ruut\n4 - suvaline\nLisa valik (1-4): "))
kujunditeArv = int(input("Mitu kujundit soovid joonistada: "))
if valik == 1:
    viisnurk(kujunditeArv)

elif valik == 2:
    ring(kujunditeArv)

elif valik ==3:
    ruut(kujunditeArv)

else:
    suvaline(kujunditeArv)







turtle.done()
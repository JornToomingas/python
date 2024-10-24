#24.10.24 Toomingas
#Ülesanne 09
import random
"""
#Genereeri ja kuva arvud arvud 1-20
for i in range(1,21):
    print(i, end= " ")


print()
#Genereeri ja kuva 20 suvalist arvu vahemikus 1-99



for i in range(1,21):
    print(random.randint(1, 99), end=" ")



#Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
#   Leia paaris ja paaritud arvud ning lisa oma loendisse
#   Kuva paaris ja paritute arvude summad
loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud = []


for i in loend:
    if i%2==0:
        paaris.append(i)
    else:
        paaritud.append(i)


print(f"Paarisarvude summa on: {sum(paaris)}")
print(f"Paaritutearvude summa on: {sum(paaritud)} ")
print()
"""

#Kuva arvud 1-42
#   Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
#   Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
#   Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)

for i in range(1,43):
    if i%3==0:
        print(i, "TIK", end=" ")
    elif i%5==0:
        print(i, "TAK", end=" ")
    else:
        print(i, end=" ")
print()


"""
jagunevad3 = ["TIK"]
if i%3==0:
    jagunevad3.append(i)
jagunevad5 = ["TAK"]
if i%5==0:
    jagunevad5.append(i)
jagunevad_molemad = ["TIKTAK"]
if i%3==0:
    jagunevad_molemad.append(i)
if i%5==0:
    jagunevad_molemad.append(i)




print()
"""

#Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.
#Kuva nimekirjast unikaalsed nimed:

# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
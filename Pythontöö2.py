#2.1 Äratus
import random
"""
kordade_arv = int(input("Mitu korda heliseda?: "))

print("\nTõuse ja sära!"*kordade_arv)

#2.2 Murelikud lapsevanemad

ringide_arv = 6
i = 1
porgandite_arv = 0
while i <= ringide_arv:
    if i%2==0:
        porgandite_arv+=i
        print(i)
    i +=1
print(f"porgandite_arv: {porgandite_arv}")

#2.3 Täringud

taringud = int(input("Mitu täringut vajad?: "))
for i in range(taringud):
    print(random.randint(1, 6))

#2.4 Male
taisarv = 10
nisutera = 0

korda = taisarv

if taisarv > 64:
    print("Nii palju ruute ei ole")

if taisarv >= 1:
    nisutera+=1
    korda-=1

while korda >= 1:
    nisutera *=2
    korda -=1

print(nisutera)
"""
#2.5 Õunad

ounu = 14
poisse = 4

for i in range(poisse):
    ounu -= random.randint(1,2)
print(ounu)
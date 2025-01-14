# Jörn Markus Toomingas 18.12.24
# Kontrolltöö
import random

#1. Korrutamise kontrollimine Jörn Markus Toomingas 18.12.24
"""
#  Korrutamise kontrollimine
# 	programm esitab korrutustehte 1p
# 	ootab kasutajalt vastuse sisestamist 1p
# 	kontrollib vastuse Ćµigsust 1p
# 	väljastab, kas vastus oli õige või väär. 1p
# 	kokku antakse lahendamiseks 10 ülesannet. 1p

#Genereerib 2 suvakat arvu ja annab korrutus tehte
a, b = random.randint(1,10), random.randint(1,10),
#Kasutaja sisestab vastuse
vastus = int(input(f"Lisa vastus {a}*{b}="))
#Kui vastus on õige
if vastus == a*b:
    print("Õige")
#Kui vastus on vale
else:
    print("Vale")
"""
#6. Paaris või paaritu Jörn Markus Toomingas 18.12.24
"""
# Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# 	kood mis teavitab paaris või paaritust arvust - 1p
# 	kuvatakse programmi pealkiri - 1p
# 	kood kommenteeritud - 1p

#Kasutaja sisestab täisarvu
arv = int(input("Sisesta number: "))
#Kui number on 0
if arv ==0:
    print("Number ei saa olla 0!")
#Kui arv on paaris
elif (arv%2) == 0:
    print("Arv on paaris")
#Kui arv on paaritu
else:
    print("Arv on paaritu")
"""
#7. Eurokalkulaator Jörn Markus Toomingas 18.12.24
"""
# Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# 	küsitakse valuuta kogust ja tehakse arvutused - 2p
# 	kood kommenteeritud - 1p

#EEK kurss
kurss = 15.6466

#Kasutaja valib kas tahab eurod kroonideks või kroonid eurodeks
suund = input("Sisestage teisendamise suund! (EUR-EEK või EEK-EUR): ")

#Kui valib eurod kroonideks
if suund == "EUR-EEK":
#Lubab sisestada komadega arvu
    eurod = float(input("Sisestage raha arv: "))
    kroonid = eurod * kurss
    print(f"{eurod} eurot on {kroonid:.2f} krooni!")

#Kui valib kroonid eurodeks
elif suund == "EEK-EUR":
#Lubab sisestada komadega arvu
    kroonid = float(input("Sisestage raha arv: "))
    eurod = kroonid / kurss
    print(f"{kroonid} krooni on {eurod:.2f} eurot!")

#Kui sisestab alguses valesti:
else:
    print("Vale sisend! Palun sisestage kas EUR-EEK või EEK-EUR")
"""
#8. Täringud Jörn Markus Toomingas 18.12.24
"""
# Täringud
# 	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# 	kasutaja võistleb kahe tĆ¤ringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p

#Täringud
def taringud():
    taring1 = random.randint(1, 6)
    taring2 = random.randint(1, 6)
    return taring1 + taring2
#
def main():
    print("Täringud kasutaja vs arvuti")

#Kasutaja paneb panuse
    while True:
        try:
            panus = float(input("Palun sisestage oma panus: "))
            if panus <= 0:
                print("Panus peab olema suurem kui 0.")
            else:
                break
        except ValueError:
            print("Palun sisestage number!")

#Kasutaja ja arvuti skoorid
kasutaja_skoor = taringud()
arvuti_skoor = taringud()

#Prindim kasutaja ja arvuti skoorid
print(f"Teie täringute summa: {kasutaja_skoor}")
print(f"Arvuti täringute summa: {arvuti_skoor}")

#Kui kasutaja võidab
if kasutaja_skoor > arvuti_skoor:
    print("Te võitsite! Saite {panus} eurot.")
#Kui arvuti võidab
elif kasutaja_skoor < arvuti_skoor:
    print("Arvuti võitis! Te kaotasite oma panuse.")
#Kui jääb viiki
else:
    print("Te jäite viiki! Teie panus jääb alles.")
"""
#16. Täringud Jörn Markus Toomingas 18.12.24

#KASUTAJA_KONTO JA ARVUTI_KONTO ANDSID UNDEFINEDVARIABLE ERRORI!!! (    EI TEA MIS SEE TÄHENDAB :(    )
"""
#  Täringud
# 	Kasutaja võistleb kahe täringuga arvuti vastu. Kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale juurde. Mäng kestab kuni kummalgi on raha otsas.
# 	(Vihjed: käsi kasutajalt nime, kuva pidevalt konto seisu ja täringuviskeid, kasutajate raha hulga mängu alguses määrad sina)


# #Täringud
def taringud():
    taring1 = random.randint(1, 6)
    taring2 = random.randint(1, 6)
    return taring1 + taring2
#
def main():
    print("Täringud kasutaja vs arvuti")
#Kasutajanimi ja kontode summad
    kasutajanimi = input("Palun sisestage oma nimi: ")
    kasutaja_konto = 100
    arvuti_konto = 100

#Kontode jääk
while kasutaja_konto > 0 and arvuti_konto > 0:
    print("\n {kasutaja_nimi}, teie kontol on {kasutaja_konto} eurot")
    print("Arvuti kontol on {arvuti_konto} eurot")


#Kasutaja paneb panuse
    while True:
        try:
            panus = float(input("Palun sisestage oma panus: "))
            if panus <= 0:
                print("Panus peab olema suurem kui 0.")
            else:
                break
        except ValueError:
            print("Palun sisestage number!")

#Kasutaja ja arvuti skoorid
kasutaja_skoor = taringud()
arvuti_skoor = taringud()

#Prindim kasutaja ja arvuti skoorid
print(f"Teie täringute summa: {kasutaja_skoor}")
print(f"Arvuti täringute summa: {arvuti_skoor}")

#Kui kasutaja võidab
if kasutaja_skoor > arvuti_skoor:
    print("Te võitsite! Saite {panus} eurot.")
    kasutaja_konto += panus
    arvuti_konto -= panus
#Kui arvuti võidab
elif kasutaja_skoor < arvuti_skoor:
    print("Arvuti võitis! Te kaotasite oma panuse.")
    kasutaja_konto -= panus
    arvuti_konto += panus
#Kui jääb viiki
else:
    print("Te jäite viiki! Teie panus jääb alles.")


if kasutaja_konto <= 0:
    print("Kahjuks sai teil raha otsa!")
elif arvuti_konto <= 0:
    print("Te võitsite! Arvutil sai raha otsa!")
"""
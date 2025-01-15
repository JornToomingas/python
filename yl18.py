#08.01.25 Jörn Markus Toomingas
#Ülesanne 18
import csv

faili_nimi = 'EstonianBasketballGames.csv'
meeskonnad = {}
with open(faili_nimi, mode='r', encoding='utf-8') as fail:

    dict_reader = csv.DictReader(fail)

    for rida in dict_reader:
        meesk1 = rida["Team 1"]
        meesk2 = rida["Team 2"]
        if meesk1 not in meeskonnad:
            meeskonnad[meesk1] = 0
        if meesk2 not in meeskonnad:
            meeskonnad[meesk2] = 0

        if meesk1 in meeskonnad:
            meeskonnad[meesk1]+=1
        if meesk2 in meeskonnad:
            meeskonnad[meesk2]+=1



print(f"osales {len(meeskonnad)} meeskonda")
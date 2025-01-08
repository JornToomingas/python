#08.01.25 Jörn Markus Toomingas
#Ülesanne 18
import csv

faili_nimi = 'EstonianBasketballGames.csv'

with open(faili_nimi, mode='r', encoding='utf-8') as fail:

    dict_reader = csv.DictReader(fail)

    for rida in dict_reader:
        meeskonnad = int(rida["Team 1"])
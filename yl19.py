#14.01.25 Jörn Markus Toomingas
#Ülesanne 19
import json


kl10 = 0
kl11 = 0
kl12 = 0



with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    opilased = json.load(file)
"""
for opilane in opilane:
    if opilane["klass"] == "12":
        opilane+=1
        print(opilane["nimi"])
        for tegevus in opilane["tegevused"]:
            print(tegevus)
        print("...............")
    if opilane["klass"] == "12":




print(f"12 löassis õpib {kl12} õpilast")
"""



for opilane in opilased:
    if opilane["klass"] == "12":
        kl12+=1
        print(opilane["nimi"])
        for trenn in opilane["tegevused"]:
            print(trenn)
            print(opilane["hinded"])
            print("-------------------------")
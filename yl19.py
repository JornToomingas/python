#14.01.25 Jörn Markus Toomingas
#Ülesanne 19
import json

kl10 = 0
kl11 = 0
kl12 = 0


with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    opilased = json.load(file)



for opilane in opilased:
    if opilane["klass"] == "12":
        kl12+=1
        print(opilane["nimi"])
        for trenn in opilane["tegevused"]:
            print(trenn)
        for aine, punktid in opilane["hinded"].items():
            print(aine, punktid)
            print("-------------------------")

print(f"12 klassis õpib {kl12} õpilast")
print(f"11 klassis õpib {kl11} õpilast")
print(f"10 klassis õpib {kl10} õpilast")
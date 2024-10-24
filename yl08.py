#24.10.24 Toomingas
#Ülesanded 


tooted = {
'piim': {'kogus': 20, 'hind': 1.19},
'küpsised': {'kogus': 20, 'hind': 4.99},
'või': {'kogus': 20, 'hind': 2.29},
'juust': {'kogus': 15, 'hind': 1.9},
'leib': {'kogus': 15, 'hind': 2.59},
'jogurt': {'kogus': 18, 'hind': 3.65},
'õunad': {'kogus': 35, 'hind': 3.15},
'apelsinid': {'kogus': 40, 'hind': 0.99},
'banaanid': {'kogus': 23, 'hind': 1.29}
}




toode = input("Sisesta toode")
toote_kogus = 10



#kas toode on olemas
if toode in tooted:
    if toote_kogus <= tooted[toode]["kogus"]:
        #kliendi arve
        print("-------------------- ARVE --------------------")
        print(f"Toode: {toode}")
        print(f"Hind: {toode[toode]["hind"]}€")
        print(f"Kogus: {toode}")
        print(f"Summa: {round(toote_kogus*tooted[toode]["hind"],2)} €")
        print("-------------------- AITÄH! --------------------")
        #laoseisu muutus
        tooted[toode]["kogus"] = tooted[toode]["kogus"] - toote_kogus
    else:
        print(f"Soovitud kogust pole. Meil on pakkuda {tooted[toode]["kogus"]} tk")
else:
    print("pole toodet")





print(tooted)
#print(tooted["piim"])
#print(tooted["piim"]["hind"])






"""
telefonid={
'Mari': '5957503',
'Toomas': '5719979',
'Kertu': '5201750',
'Siim': '5580027',
'Piret': '5960799',
'Jaan': '5160415',
'Lea': '5760164',
'Mart': '5337951',
'Anni': '5004818',
'Tõnu': '5721873',
'Kai': '5811884',
'Rasmus': '5859489',
'Eva': '5039393',
'Oskar': '5635812',
'Liina': '5696114',
'Peeter': '5560756',
'Sandra': '5257415',
'Heiki': '5207248',
'Kristi': '5703338',
'Urmas': '5400549'
}



print(telefonid["Rasmus"])
telefonid["Mario"]="42646446677"
telefonid.pop("Kristi")
telefonid["Eva"]="5555555555"
print(telefonid)





valik = input("Otsi kontakt: ")
try: 
    print(f"{valik} tel nr. on: {telefonid[valik]}")
except:
    print(f"{valik} tel nr. pole")
"""
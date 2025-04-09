# Jörn Markus Toomingas 09.04.25
# Kontrolltöö 3
import requests

url = f"https://metshein.com/kordamine/json/autod.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    autod = data
    leitud = False

    id_sisestus = int(input("Palun sisestage ID (1-20): "))

    try:
        user = autod[id_sisestus - 1]
        print(f"Role ID: {user['id']}")
        print(f"Mark: {user['mark']}")
        print(f"Mudel: {user['mudel']}")
        leitud = True
    except IndexError:
        print("Sisestatud id pole õige")
else:
    print("Viga andmete laadimisel", response.status_code)
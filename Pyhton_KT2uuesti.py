#Jörn Markus Toomingas 27.01.25
#Kontrolltöö 2 uuesti
import requests

url = f"https://dummy-json.mock.beeceptor.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    users = data
    leitud = False

    id_sisestus = int(input("Palun sisestage ID (1-20): "))

    try:
        user = users[id_sisestus - 1]
        print(f"Role ID: {user['id']}")
        print(f"Nimi: {user['name']}")
        print(f"Firma: {user['company']}")
        print(f"Kasutajanimi: {user['username']}")
        print(f"Email: {user['email']}")
        print(f"Aadress: {user['address']}")
        leitud = True
    except IndexError:
        print("Sisestatud id pole õige")
else:
    print("Viga andmete laadimisel", response.status_code)
#Jörn Markus Toomingas 27.01.25
#Kontrolltöö 2 uuesti
import requests

url = f"https://dummy-json.mock.beeceptor.com/roles"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    data = data["id"]

    id = int(input("Palun sisestage ID (1-5)"))
    print(data[id])

    for role in data:
        if role["id"] == id:
            print(f"Role ID: {role['id']}")
            print(f"Role Name: {role['name']}")
            print(f"Description: {role['description']}")
else:
    print("Role not found :( )")
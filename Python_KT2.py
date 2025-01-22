# Jörn Markus Toomingas 22.01.24
# Kontrolltöö
import requests
import json
url = f"https://dummyjson.com/products"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    data = data["products"]

    id = int(input("Sistestage ID: "))
    print(data[1])
    # for toode in data:
    #    if toode['id'] == id:
    #         print(f"id: {data['id']}")
    #         print(f"title: {data['title']}")
    #         print(f"category: {data['category']}")
    #         print(f"price: {data['price']}")
    #         print(f"rating: {data['rating']}")
    #         print(f"stock: {data['stock']}")
    #         break
    # else:
    #    print("Toodet ei leitud.")
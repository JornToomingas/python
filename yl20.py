#15.01.25 Jörn Markus Toomingas
#Ülesanne 20
import requests

kysimus = input("Linnanimi: ")
city = kysimus
api_key = "6b1983932b639eff2aae7b442aaad779"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Ilma kirjeldus: {weather}")
    print(f"Temperatuur: {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)
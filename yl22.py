#28.01.25 Jörn Markus Toomingas
#Ülesanne 22
import locale
from datetime import datetime, date
#1. Lihtne kuupäev
now = datetime.now()
synniaeg = datetime(2008, 7, 2)
print("Praegune aeg: ", now.strftime("%d.%m.%Y %H:%M:%S"))
difference = now - synniaeg
print("Kuupäevade vahe päevades: ", difference.days)
print("Kuupäevade vahe aastates: ", int(difference.days/365), "aastat")

#2. Autorent
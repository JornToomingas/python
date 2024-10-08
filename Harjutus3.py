# Jörn Markus Toomingas 08.10.24
# Harjutus 03

import turtle

"""
Ülesanne 3.1: Tervitus
Loo muutuja nimi, mis sisaldab kasutaja nime (string)
Loo muutuja vanus, mis sisaldab kasutaja vanust (integer)
Loo muutuja keskmine_hinne, mis sisaldab kasutaja keskmist hinnet (float)
Trüki välja lause, mis ühendab kõik kolm muutujat, nt: “Karin, 18 aastat vana ja keskmine hinne on 4.7”
"""

nimi = "Üllar"
vanus = 18
keskmine_hinne = 3.8
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine_hinne))

"""
Ülesanne 3.2: Ostunimekiri
Loo muutuja toode, mis sisaldab toote nime (string)
Loo muutuja kogus, mis näitab, mitu toodet soovitakse osta (integer)
Loo muutuja hind, mis näitab ühe toote hinda (float)
Trüki välja lause, mis ühendab need andmed, nt: “Soovin porgandeid 3, mille tüki hind on 5 eurot.”
"""

toode = "porgandeid"
kogus = 3
hind = 5.0

print("Soovin "+ str(toode) +" " +str(kogus)+",mille tüki hind on "+str(hind)+" eurot.")


"""
Ülesanne 3.3: Reisiplaan
Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)
Trüki välja lause, mis ühendab need andmed, nt: “Minu reis Soome kestab 5 päeva ja üks öö maksab 30.50 eurot.”
"""

"""
Ülesanne 3.4: Lemmikraamat
Loo muutuja raamatu_pealkiri, mis sisaldab raamatu pealkirja (string)
Loo muutuja lehekylgede_arv, mis näitab raamatu lehekülgede arvu (integer)
Loo muutuja hindamisskoor, mis näitab raamatu hinnet skaalal 1-10 (float)
Trüki välja lause, nt: “Minu lemmikraamat on Sipsik, mis on 16 lehekülge pikk ja mille ma hindan 9.7 punktiga.”
"""

"""
Ülesanne 3.5: Unistuste auto
Loo muutuja auto_mark, mis sisaldab auto marki (string)
Loo muutuja tootmisaasta, mis näitab auto tootmisaastat (integer)
Loo muutuja hind, mis näitab auto hinda (float)
Trüki välja lause, nt: “Minu unistuste auto on Opel aastast 1996, mille hind on 150.90 eurot.”
"""

"""
Ülesanne 3.6: Python Turtle
Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
Loo muutuja kujundi_varv, mis määrab kujundi täitevärvi (string)
Kasutades Turtle’i, joonista kõrvuti värvilised kujundid ruut ja kolmnurk, mis kasutab loodud muutujaid
"""

kylg = 100
varv = "green"

turtle.color(varv)
turtle.fd(kylg)
turtle.left(90)
turtle.fd(kylg)
turtle.left(90)
turtle.fd(kylg)
turtle.left(90)
turtle.fd(kylg)
turtle.left(90)

#liigu
turtle.penup()
turtle.goto(kylg*1.5,0) # poole võrra alati eemal
turtle.pendown()

#kolmnurk
turtle.color(varv)
turtle.fd(kylg)
turtle.left(120)
turtle.fd(kylg)
turtle.left(120)
turtle.fd(kylg)
turtle.left(120)


turtle.done()
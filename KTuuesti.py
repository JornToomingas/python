#Jörn Markus Toomingas 07.01.25
#Kontrolltöö 


#3. Einstein
"""
#sisestad massi
m = int(input("Palun sisestage arv: "))
#valguse kiirus
c = 300000000 #m/s

#arvutus ja väljastus
E = m * c**2
print(E, "MJ")

"""
#9. Coca-Cola automaat
"""
def coca_automaat():
#alguses olevad mündid
    mündid = 0
    while mündid < 50:
#Küsib kasutajalt münte
        münt = int(input("Sisesta münte: "))
#Kui mündid on antud summas lisab juurde muidu keeldub ja küsib uuesti
        if münt in [25, 10, 5]:
            mündid += münt
            vajatud = 50 - mündid
#Kui on veel vaja münte
        if vajatud > 0:
            print(f"Veel on vaja {vajatud} senti")
    else:
        print("Palun sisestage mündid uuesti.")
#Vahetusraha
    vahetusraha = mündid - 50
    print(f"Tagastatakse {vahetusraha} senti.")

coca_automaat()
"""
#10. twttr
"""
#Eemaldab täishäälikud
def eemalda_täishäälikud(tekst):
    täishäälikud = "AEIOUaeiou"
    tulemus = ''.join(täht for täht in tekst if täht not in täishäälikud)
    return tulemus

#Tekst mis kasutaja sisestab
tekst = input("Sisesta tekst: ")
tulemus = eemalda_täishäälikud(tekst)
print("Tekst ilma täishäälikuteta", tulemus)
"""
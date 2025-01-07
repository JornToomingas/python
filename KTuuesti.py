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
    mündid = 0
    while mündid < 50:
        münt = int(input("Sisesta münte: "))
        if münt in [25, 10, 5]:
            mündid += münt
            vajatud = 50 - mündid
        if vajatud > 0:
            print(f"Veel on vaja {vajatud} senti")
    else:
        print("Palun sisestage mündid uuesti.")

    vahetusraha = mündid - 50
    print(f"Tagastatakse {vahetusraha} senti.")

coca_automaat()
"""
#10. twttr

# def eemalda_täishäälikud(tekst):
täishäälikud = "AEIOUaeiou"
tulemus = ''.join(täht for täht in tekst if täht not in täishäälikud)
# return tulemus

tekst = input("Sisesta tekst: ")
tulemus = eemalda_täishäälikud(tekst)
print("Tekst ilma täishäälikuteta", tulemus)
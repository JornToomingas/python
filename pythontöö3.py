#3.1 Ülikooli vastuvõetud

fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
print(vastuvõetud)

fail.close()

a = input("Palun sisestage, millise aasta andmeid vajate?: ")

print(vastuvõetud[int(a[3])-1])




#3.2 Jänesevanemate mure vol. 3


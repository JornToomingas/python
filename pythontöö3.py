#3.1 Ülikooli vastuvõetud
"""
fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
print(vastuvõetud)

fail.close()

a = input("Palun sisestage, millise aasta andmeid vajate?: ")

print(vastuvõetud[int(a[3])-1])




#3.2 Jänesevanemate mure vol. 3

fail = open("konto.txt", encoding = "UTF-8")

for rida in fail:
    if float(rida) > 0:
        print(rida, end="")


"""
#3.3 

fail = open("konto.txt", encoding = "UTF-8")

tehingud = []

for rida in fail:
    tehingud.append(rida)
print(tehingud)

fail.close()
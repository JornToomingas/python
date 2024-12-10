# 4.1 Bänner

sg = int(input("Mitu korda soovitakse lauset kuvada: "))
sf = (input("Millist reklaamlauset soovite kasutada: "))

def banner(x, y):
    for i in range(x):
        print(y.upper())

banner(sg, sf)

# 4.2 Õunamahla tegemine

def mahlapakkide_arv(kg):
    arv = round(kg * 0.4/3,0)
    return arv

ounad = int(input("Õunte kogus: "))

print(mahlapakkide_arv(ounad))
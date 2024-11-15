#08.11.24 Toomingas
#Ülesanne 12
import turtle
"""
#1.
def temperatuur(temp, yhik):
    
    See on maailma parim manual
    Parameetrid: kui ei tea
    Näide: uuri ise
    
    if yhik=="c":
        v = temp * 5/9 + 32
    else:
        v = (temp -32 * 5/9)
    return round(v,2)

print(temperatuur(3,"c"))
print(temperatuur(3,"f"))
print(temperatuur.__doc__)
"""


"""
#2.
kytuskulu = lambda x, y: (x/100) * y
print(kytusekulu(5,150))
"""


#3.
pangakonto = 15

def konto_haldur(saldo, toiming, summa):
    """
    Eriti oluline dokumentatsioon, et kõik aru saaks
    """
    global pangakonto
    if toiming=="deposiit":
        summa = summa + saldo     #summa+=saldo
    else:
        summa = summa - saldo

    pangakonto = summa
    return summa




print(konto_haldur(20,"deposiit", pangakonto))
print(konto_haldur(40,"deposiit", pangakonto))
print(konto_haldur(50,"välavõte", pangakonto))
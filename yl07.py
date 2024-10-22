#22.10.24 Toomingas
#Ülesanne 7


import datetime



# 12 kuud
kuud = [["jaanuar",-10,22,11,20,17,-5,24,-2,15,-7,9,17,-16,5,15,25,-9,-5,28,26,-3,5,30,2,9,15,-5,-19,0,18,14],
["veebruar",5,15,19,-18,-1,-8,18,22,-14,-13,27,-10,12,7,-15,10,-1,-12,2,-5,7,13,-17,26,10,-20,14,-13,22,1,15],
["märts",-14,-8,-8,22,16,6,3,25,11,-1,0,8,29,21,27,-8,8,-17,23,21,13,-2,11,-16,11,29,-3,26,4,4,14],
["aprill",12,20,-10,-9,-1,29,6,15,9,1,17,-17,30,-4,2,20,-6,-18,26,-4,-4,-16,17,-4,21,15,25,5,-2,19,30],
["mai",17,6,17,27,25,26,6,4,-10,27,24,-13,-15,28,20,9,10,1,23,-13,-9,30,6,8,-15,4,12,-1,18,4,26],
["juuni",-20,-10,8,-20,7,-11,-9,8,-16,-17,16,18,4,-4,-14,6,9,-17,30,-15,-20,-4,28,19,-12,-3,21,-18,28,-11,16],
["juuli",19,24,-11,18,8,10,-10,23,-16,-8,7,-7,2,-6,-14,14,9,-20,-19,-14,12,20,2,23,-16,26,-14,25,11,12,13],
["august",-7,27,-16,-11,10,18,15,7,-1,-10,18,20,10,8,23,-3,-19,-11,-7,9,30,-14,12,19,15,25,-15,2,14,10,20],
["september",-1,7,1,-15,1,30,26,-1,4,-10,0,5,17,25,8,-6,-8,25,10,-7,-18,-18,23,15,-11,-17,-5,-3,6,-9,7],
["oktoober",8,2,18,5,0,15,25,-10,23,-6,28,24,-20,4,-15,-1,22,-11,30,28,22,14,30,-17,-17,-13,5,24,22,26,3],
["november",20,21,15,28,-8,-9,9,-20,14,5,25,-12,30,27,-17,-12,4,12,3,-12,10,-11,-18,0,3,19,-6,-2,29,9,15],
["detsember",-15,11,-6,1,21,14,-4,-7,27,-11,0,-20,9,-8,26,-8,0,29,12,13,1,-19,3,13,-2,-2,6,19,-14,22,9]]



x = datetime.datetime.now()
tana = int(x.strftime("%m")) -1 # -1 et loendiga ühildada



#tänase kuu andmed

ajutine = []
print(kuud[tana][0])
print(f"Viimane mõõtmine sellel kuul: {kuud[tana][len(kuud[tana])-1]}")
for i in range(len(kuud[tana])-1):
    ajutine.append(kuud[tana][i+1])
    print(kuud[tana][i+1], end=", ")

print()
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")
print(f"Keskimne temp: {round(sum(ajutine)/len(ajutine),2)}")


print(f"-20 esineb {ajutine.count(-20,ajutine)} korda")

ajutine.pop(5)
print(ajutine)



muusika = ['ALIKA – "Bridges”','Anett x Fredi – "Read Between The Lines”','villemdrillem – "leekiv armastus”','Clicherik & Mäx – "PAKSUD”','nublu – "ära ärata”','NOËP – "Move Your Feet”','Trad.Attack! – "Bring It On”','Bedwetters – "It Is What It Is”','Reket – "Panama paberid”','Grete Paia – "Võluväel”']


"""
for i in range(len(muusika)):
    print(str(i+1)+". "+muusika[i])


try:
    valik= int(input("Vali laul"))
    print(f"Mängin lugu {muusika[valik-1]}")

except:
    print  ("Midagi läks katki. Teavita adminni")
"""
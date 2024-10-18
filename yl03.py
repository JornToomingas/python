#16.10.24 Toomingas
#Ülesanne03
import turtle

#Ülesanne 3.2: Ostunimekiri










#Ülesanne 3.4:Lemmikraamat





raamatu_pealkiri = "Kullamõistatus"
raamatu_autor = "Martin Widmark"
raamat = raamatu_pealkiri+" "+ raamatu_autor
lehekylgede_arv = 96
hindamisskoor = 9.5

print("Minu lemmikraamat on",raamat,",mis on", lehekylgede_arv,"pikk ja mille ma hindan",hindamisskoor,"punktiga.")



#Ülesanne 3.5: Unistuste auto
mark, mudel = "porsche", "911"
auto = mark+" "+mudel
aasta = 1980
hind = 60000

print("Minu unistuste auto on",auto,"aastast",aasta,",mille hind on",hind,"eurot.")


#ülesanne 3.6: Python Turtle ruut

"""

kylje_pikkus =90
nurk = 90
kujundi_varv = "purple"


turtle.color(kujundi_varv)

for i in range(3):
    for i in range(3):
        turtle.fw(kylje_pikkus)
    turtle.left(nurk)

    turtle.penup()
    turtle.fw(kylje_pikkus*1.5)
    turtle.pendown()

turtle.done()

"""
#Ülesanne 3.7: Python Turtle kolmnurk
"""

kylje_pikkus = 100
nurk = 120
kujundi_varv = "blue"

turtle.color(kujundi_varv)

for i in range(3):
    for i in range(3):
        turtle.forward(kylje_pikkus)
        turtle.left(nurk)

    turtle.penup()
    turtle.forward(kylje_pikkus*1.5)
    turtle.pendown()

turtle.done()

"""
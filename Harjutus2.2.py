# Jörn Markus Toomingas
# Harjutus 02.2
# Sinilill

import turtle
aken = turtle.Screen()
aken.setup(width=500,height=500)
aken.title("Sinilill - Jörn Markus Toomingas")
turtle.speed("fastest")
turtle.pensize(10)

#vars
turtle.pencolor("green")
turtle.left(90)
turtle.fd(-150)
turtle.fd(200)

#õis
turtle.begin_fill()
turtle.color("blue","lightblue")
turtle.right(90)
turtle.circle(60)
turtle.end_fill()


turtle.left(90)
turtle.penup()
turtle.fd(50)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow","yellow")
turtle.right(90)
turtle.circle(10)
turtle.end_fill()

#leht
turtle.begin_fill()
turtle.color("green","green")
turtle.penup()
turtle.goto(-20,-50)
turtle.pendown()
turtle.left(90)
turtle.fd(40)
turtle.left(120)
turtle.fd(40)
turtle.left(120)
turtle.fd(40)
turtle.left(120)
turtle.end_fill()

turtle.done()
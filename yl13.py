#15.11.24 Toomingas
#Ülesanne 13


import turtle




screen = turtle.Screen()
t = turtle.Turtle()



#küsi kasutajalt numbrilist sisendit
# vanus = screen.numinput("Vanuse sisestamine", "Mis on sinu vanus?", default=20, minval=0, maxval=100)
nr = 10
turtle.speed(0)
for i in range(nr*10):
    turtle.lt(90)
    turtle.fd(3)
    turtle.lt(180)
    turtle.fd(3)
    turtle.lt(90)
    turtle.fd(4)
turtle.goto(0, 0)
for i in range(nr+1):
    turtle.lt(90)
    turtle.fd(5)
    turtle.write(i, font=("Arial", 10, "normal"))
    turtle.lt(180)
    turtle.fd(5)
    turtle.lt(90)
    turtle.fd(10*4)
turtle.done()
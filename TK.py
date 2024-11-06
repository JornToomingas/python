#06.11.24
#TK nr 6,4,1 Toomingas


import turtle
turtle.speed(5)
"""
#1
d = 90
for i in range(4):
    turtle.fd(d)
    turtle.left(90)
    turtle.fd(d)
    turtle.right(90)
    turtle.fd(d)
    turtle.left(90)
"""


#4
d = 60
for i in range(5):
    turtle.left(360/5)
    for i in range(4):
        turtle.fd(d)
        turtle.left(90)



"""
#6
d = 120
for i in range(4):
    turtle.lt(90)
    for i in range(2):
        turtle.fd(d)
        turtle.left(90)
        turtle.fd(d/2)
        turtle.left(90)
"""

turtle.done()
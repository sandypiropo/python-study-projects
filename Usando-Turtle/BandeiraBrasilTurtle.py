# Brazill Flag

from turtle import *

speed(0)
setup(800, 500)
title("Brazil flag")
bgcolor('green')


# Losango
size = 370
t1 = Turtle()
t1.pencolor('yellow')
t1.fillcolor('yellow')
t1.begin_fill()

t1.penup()
t1.goto(-0, 190)
t1.pendown()

t1.right(150)
t1.forward(size)
t1.left(120)
t1.forward(size)
t1.left(60)
t1.forward(size)
t1.left(120)
t1.forward(size)
t1.end_fill()

# Circulo
t2 = Turtle()
t2.pencolor('blue')
t2.fillcolor('blue')
t2.begin_fill()

radius = 120

t2.penup()
t2.goto(-0, -110)
t2.pendown()

t2.circle(radius)
t2.end_fill()

done()
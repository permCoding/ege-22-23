from turtle import *

step = 60
shape("turtle")
left(90)

x0, y0 = -200, -200

penup()
goto(x0, y0)
pendown()

color("red")
width(2)
speed(7)

for i in range(3):  # там было 7
    forward(10 * step)
    right(120)

penup()
for x in range(10):
    for y in range(11):
        setpos(x0 + x*step, y0 + y*step)
        dot(5, "black")

from turtle import *

color('red', 'yellow')
shape('turtle')
speed(0)
left(90)
x0, y0 = -200, -200
penup()
goto(x0, y0)
pendown()
step = 50

begin_fill()
for _ in range(7):
    forward(10*step)
    right(120)
end_fill()

penup()
for x in range(12):
    for y in range(12):
        setpos(x0+x*step, y0+y*step)
        dot(3, 'black')

done()

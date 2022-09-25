from turtle import *

speed(6)
width(3)
step = 10
shape("turtle")
color("green")
left(90)

pendown()
i = 0
while i < 26:
    forward(5*step)
    left(45)
    backward(5*step)
    right(30)
    i = i + 1  # i += 1

done()

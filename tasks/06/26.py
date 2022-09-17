from turtle import *

step = 15
color("red")
width(2)
speed(0)

for i in range(26):
    forward(5 * step)
    left(45)
    backward(5 * step)
    right(30)

done()

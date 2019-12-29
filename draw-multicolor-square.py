# Square with differt colr for each side

import turtle
fred = turtle.Turtle()

fred.speed(2)
fred.width(6)

for color in ["green", "orange", "blue", "red"]:
    fred.color(color)
    fred.forward(100)
    fred.right(90)
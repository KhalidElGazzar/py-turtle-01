import turtle
fred = turtle.Turtle()

# set width of pen: Thickest: 10, Thinest: 1
fred.width(8)

# set turtle speed - fast: 10, slowest 1
fred.speed(2)

angle = 180-45

# Draw Octagram (8 sides star)
for i in range (0, 8):
    fred.forward(200)
    fred.right(angle)

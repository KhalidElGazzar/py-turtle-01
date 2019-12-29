import turtle

ted = turtle.Turtle()
ted.color("red")
ted.width(5)
ted.speed(3)

sides = 20
length = 50

ted.penup()
ted.goto(0, length*2)
ted. pendown()

# Draw Circlular shape
for i in range(sides):
    ted.forward(length)
    ted.right(360/sides)

ted.penup()
ted.goto(length, -length)
ted.pendown()
ted.color("green")


# Draw Spiral
for i in range(100):
    ted.forward(i)
    ted.right(360/sides)    # try angle of 75 - beautiful


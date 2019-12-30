"""
The rules
Before you start coding, let's make sure the basic idea of Fizz Buzz is clear. You count up through a series of numbers (0, 1, 2, 3, 4, 5 ... ) and for each number:

If the number is evenly divisible by 3, you say "Fizz"
If the number is evenly divisible by 5, you say "Buzz"
If the number is evenly divisible by both 3 and 5, you say "FizzBuzz"
"""

import turtle
tur = turtle.Turtle()

def fizz():
    # A red square bead.
    tur.color("red")
    tur.left(90)
    for side in [10, 20, 20, 20, 10]:
        tur.forward(side)
        tur.right(90)

def buzz():
    # A green hexagonal bead.
    # Fits inside the red bead.
    tur.color("green")
    tur.left(60)
    for side in range(6):
        tur.forward(10)
        tur.right(60)
    tur.right(60)

def plain():
    # A gray octagonal bead.
    tur.color("gray")
    tur.left(90)
    for side in [4, 8, 8, 8, 8, 8, 8, 8, 4]:
        tur.forward(side)
        tur.right(45)
    tur.right(45)

tur.penup()
tur.back(120)
tur.pendown()
tur.width(2)

for i in range(20):
    if i % 3 == 0 and i % 5 == 0:
        fizz()
        buzz()
    else:
        if i % 3 == 0:
            fizz()
        elif i % 5 == 0:
            buzz()
        else:
            plain()
    # Advance to the next bead spot.
    tur.color("gray")
    tur.forward(22)

tur.hideturtle()

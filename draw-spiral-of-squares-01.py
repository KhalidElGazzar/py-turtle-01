import turtle
jack = turtle.Turtle()

jack.color("blue")
jack.width(2)

def draw_square():
   for i in range (4):
        jack.forward(100)
        jack.right(90) # use right or left
        
# draw_square()

jack.speed(0)
for square in range(80):
    draw_square()
    jack.forward(5)
    jack.left(5)
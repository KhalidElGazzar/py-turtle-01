import turtle
ted = turtle.Turtle()
tedWidth, tedSpeed = (10, 8)
ted.speed(tedSpeed)
ted.width(tedWidth)

'''
    placeTurtle() is a function to place a cursor in a certain location on canvas
    params: 
        x:  int - xpos
        y:  int - ypos
'''
def placeTurtle(x,y):
    ted.penup()
    ted.setpos(x,y)
    ted.pendown()

placeTurtle(-240, 240)

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
for color in rainbow:
    ted.color(color)
    ted.forward(100)
    ted.right(60)

placeTurtle (240,240)
for color in rainbow:
    ted.color(color)
    ted.forward(100)
    ted.penup()
    ted.sety(ted.ycor()-tedWidth)
    ted.back(100)
    ted.pendown()    
    
angle = 180-36
placeTurtle (0,0)
for color in rainbow:
    ted.color(color)
    for i in range (0, 5):
        ted.forward(100)
        ted.right(angle)
    ted.penup()
    ted.forward(150)
    ted.right(60)
    ted.pendown()

ted.hideturtle()
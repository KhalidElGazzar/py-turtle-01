import turtle
amy = turtle.Turtle()
amy.speed(3)

'''
    drawLine() is a function to draw a line in certain color
    params: 
        color:      string - color of the pen
        distance:   int - length of the line
'''
def drawLine(color, distance):
    amy.color(color)
    amy.forward(distance)

"""
    moveWithoutDrawing() is a function to move the turtle forward or backward for a certain distance without drawing
    params: 
        distance:   int - distance in pixels for the turtle to move 
        direction:  int - 
                        < 0 (-ve value)  : means backwards
                        any other value  : means forward
"""
def moveWithoutDrawing(distance, direction):
    amy.penup()
    if direction < 0:
        # move backwards
        amy.back(distance)
    else:
        # move forward
        amy.forward(distance)
    amy.pendown()


# Make the width thicker so that the line will be easier to see
amy.width(8)

# Move back without drawing anything
moveWithoutDrawing(100, -1)

# Draw a red line
drawLine("red",50)

# Move forward without drawing anything
moveWithoutDrawing(25, 1)

# Draw an orange line
drawLine("orange",50)

# Move forward without drawing anything
moveWithoutDrawing(25, 1)

# Draw a yellow line
drawLine("yellow",50)

amy.hideturtle()
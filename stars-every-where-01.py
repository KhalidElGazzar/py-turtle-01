import turtle
ted = turtle.Turtle()
ted.speed(0)

def prepareDrawingPosition():
    ted.penup()
    ted.right(180)
    ted.right( 180 * x / 5 + (0.5 * 180/5)) 
    ted.forward(distance)
    ted.pendown()

def drawStar(sideLength, color, width):
    for i in range(5):
        ted.color(color)
        ted.width(width)
        ted.forward(sideLength)
        ted.right(180-36)

for distance in [125, 75]:
    if distance == 125:
        tedColor = "red"
        starEdge = 50
        tedWidth = 4
    else:
        tedColor = "blue"
        starEdge = 30
        tedWidth = 5

    for x in range(5):    
        prepareDrawingPosition()
        drawStar(starEdge, tedColor, tedWidth)
        ted.penup()
        ted.home()

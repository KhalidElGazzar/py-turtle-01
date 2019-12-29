import turtle

links = [1, 2, 3, 4, 5, 6, 7, 8]
sides = [1, 2, 3, 4, 5, 6]

weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')

# Move back so the chain is centered.
weaver.penup()
weaver.back(180)
weaver.pendown()

for link in links:
    # Draw a hexagon.
    for side in sides:
        weaver.forward(30)
        weaver.right(60)

    # Scoot over to the next link.
    weaver.penup()
    weaver.forward(60)
    weaver.pendown()

weaver.hideturtle()


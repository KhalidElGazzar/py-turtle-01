import turtle

links = [1, 2, 3, 4, 5, 6,]
sides = [1, 2, 3, 4, 5, 6]

weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')

# Move back so the chain is centered.
weaver.penup()
weaver.back(80)
weaver.pendown()

for link in links:
    # Draw a hexagon.
    for side in sides:
        weaver.forward(30)
        weaver.right(60)

    # Scoot over to the next link.
    # weaver.penup()
    weaver.right(120)
    # use distmce of 10 or 15, or 20 to widen / shriken the star
    weaver.forward(15) # 10 or 15 or 20. You can even add more
    weaver.left(60)
    weaver.pendown()

weaver.hideturtle()

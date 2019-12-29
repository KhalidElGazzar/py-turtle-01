import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.forward(-140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
  amy.color(prettycolor)
  
  # draw square
  for i in [1,2,3,4]:
    amy.forward(50)
    amy.right(90)
    
  amy.penup()
  amy.forward(75) # 1.5 times the side
  amy.pendown()
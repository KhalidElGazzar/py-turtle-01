import turtle

fred = turtle.Turtle()
fred.color("green")

# for i in range(0, 4):  

sides = [1, 2, 3, 4]
for i in sides:  
    fred.forward(100)
    fred.right(90)
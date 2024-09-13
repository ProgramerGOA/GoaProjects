
from turtle import *

# Draw the square for the house
shape("turtle")
width(7)
color("purple")

for _ in range(4):
    forward(200)
    left(90)

# Draw the door
penup()
goto(70, -100)  # Position the turtle to start drawing the door
pendown()
color("yellow")
begin_fill()
for _ in range(2):
    forward(120)  # Height of the door
    left(90)
    forward(60)
    left(90)
end_fill()



# Draw the roof
penup()
goto(-100, 200)  # Position the turtle to start drawing the roof
pendown()
color("red")
begin_fill()
left(150)
forward(200)
left(120)
forward(200)
end_fill()

exitonclick()
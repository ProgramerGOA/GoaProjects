from  turtle import *

#we went to paint a house

#step 1: draw a square
shape("turtle")
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


#end of square

#drawing a door

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200, 200)
pendown()

color("Red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(50,130)
pendown()


right(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)


penup()
goto(150,130)
pendown()


left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)




exitonclick()
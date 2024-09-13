
import turtle

# Настройки
window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor("skyblue")

pen = turtle.Turtle()
pen.speed(5)
pen.color("black")
pen.penup()

# Рисуем основание дома
pen.goto(-100, -100)
pen.pendown()
pen.begin_fill()
pen.color("lightgreen")
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# Рисуем крышу
pen.setheading(45)
pen.begin_fill()
pen.color("brown")
pen.goto(-100, 100)
pen.goto(0, 200)
pen.goto(100, 100)
pen.goto(-100, 100)
pen.end_fill()

# Рисуем дверь
pen.penup()
pen.goto(-30, -100)
pen.pendown()
pen.begin_fill()
pen.color("brown")
pen.setheading(90)
pen.forward(80)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(80)
pen.end_fill()

# Рисуем окно
pen.penup()
pen.goto(30, 0)
pen.pendown()
pen.begin_fill()
pen.color("blue")
for _ in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

# Закрываем окно
pen.penup()
pen.goto(30, 0)
pen.pendown()
pen.color("white")
pen.goto(55, 25)
pen.penup()
pen.goto(30, 25)
pen.pendown()
pen.goto(55, 0)

# Закрываем дверь
pen.penup()
pen.goto(-10, -100)
pen.pendown()
pen.color("white")
pen.goto(10, -100)

# Закрываем программу
window.mainloop()


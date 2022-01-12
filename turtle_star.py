"""Draw 5 stars using turtle"""
import turtle
sc = turtle.Screen()
turtle.speed(0)
col = ["red", "yellow", "orange", "blue", "green"]
for i in range(5):
    turtle.color("black", col[i])
    turtle.begin_fill()
    for p in range(5):
        turtle.forward(100)
        turtle.right(150)
        turtle.forward(100)
        turtle.left(150)
        turtle.right(360 / 5)
        turtle.right(2)
    turtle.end_fill()
turtle.hideturtle()

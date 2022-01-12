"""Draw a rainbow using turtle"""
import turtle

sc = turtle.Screen()
pen = turtle.Turtle()


def semi_circle(col, rad, val):
    pen.color(col)
    pen.circle(rad, -180)
    pen.up()
    pen.setpos(val, 0)
    pen.down()
    pen.right(180)


col = ["red", "yellow", "orange", "blue", "green", "violet", "indigo"]
sc.setup(600, 600)
sc.bgcolor("black")
pen.right(90)
pen.speed(7)
pen.width(10)

for i in range(15):
    semi_circle(col[i], 10*(i + 8), -10*(i + 1))

pen.hideturtle()

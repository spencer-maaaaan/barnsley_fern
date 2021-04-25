"""
auth spencer tenney
desc grows a barnsley tree with a turtle
"""
from barnsley_generator import barnsley_generator
import turtle

pen = turtle.Turtle()
pen.color("green")
pen.penup()
pen.speed(15)

fern = barnsley_generator()

for point in fern:
    x,y = point

    pen.goto(90*x,75*y-400)
    pen.pendown()
    pen.dot()
    pen.penup()

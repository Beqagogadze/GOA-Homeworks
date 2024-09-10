from turtle import *

speed(0)
width(6)

def draw_square():
    for i in range(4):
        forward(300)
        left(90)
draw_square()

def move(x, y):
    penup()
    goto(x, y)
    pendown()

move(-320, 0)
draw_square()    

move(-320, -320)
draw_square()

move(0, -320)
draw_square()

exitonclick()
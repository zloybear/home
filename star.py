import turtle
from turtle import*
def star():
    color('red2')
    begin_fill()
    for i in range(5):
        forward(100)
        left(145)
    end_fill()
star()
up()
goto(100,100)
down()
star()
up()
goto(-100,-100)
down()
star()

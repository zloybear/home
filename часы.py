import turtle
from turtle import*
def jump(distance,angle=0):
    up()
    right(angle)
    forward(distance)
    left(angle)
    down()
def dial(radius):
    pensize(10)
    for i in range(60):
        jump(radius)
        if i %5==0:
             forward(10)
             jump((radius+10)*-1)
        else:
             dot(5)
             jump(radius*-1)
        right(6)
def arrow(dlina,dlinaot):
    down()
    pensize(8)
    forward(dlina)
    pensize(1)
    right(150)
    begin_fill()
    for i in range(3):
        forward(dlinaot)
        right(120)
    end_fill()
tracer(False)
dial(200)
arrow(150,30)
up()
forwad(200)
updatae()

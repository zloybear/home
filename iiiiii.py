import turtle
from turtle import*
import random
def star(x,y,listcolor):
    for i in range(len(listcolor)):
        up()
        goto(x+i*100,y+i*50)
        down()
        color(listcolor[i])
        begin_fill()
        for i in range(5):
            left(144)
            forward(100)
        end_fill()
def circ ():
    for i in range(50):
        forward((i+0.01)*0.05)
        left(1)


def s ():
    b=Turtle(shape='circle')
    b.speed(100)
    b.up()
    b.goto(-250,250)
    b.down()
    b.pensize(10)
    b.right(90)
    b.forward(450)
    b.left(90)
    b.forward(450)
    b.left(90)
    b.forward(450)

    b.color('cyan')
    speedX=random.randint(-3,3)
    speedY=random.randint(-3,3)
    gravitation=0.1
    b.up()
    b.goto(random.randint(-200,200),random.randint(-200,200))

    while True:
            speedY-=gravitation
    if b.ycor()<=-200:
            speedY*=-1
    if b.xcor()<=-250:
            speedX*=-1
    if b.xcor()>=200:
            speedX*=-1
    b.goto(b.xcor()+speedX,b.ycor()+speedY)

speed(0)
listcolor1=['#119933','#aaaa00','#ff00ff','#dd00aa','#994455','#211355']
star(-200,-200,listcolor1)
s()

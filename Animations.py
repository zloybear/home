from turtle import *
from random import *

speed(0)
up()
goto(-250, 250)
down()
right(90)
forward(450)
left(90)
forward(450)
left(90)
forward(450)

y=randint(100,200)
x=randint(-200,200)

xSpeed=randrange(-5,5,2)
ySpeed=randint(1,5)

gravity=0.2

b=10
points=0

ball=Turtle(shape='circle')
ball.color('purple2')
ball.up()
ball.speed(0)
ball.goto(x,y)
ball.speed(1.5)

infinit=1

while True:
    ball.goto(x,y)
    if ball.xcor()>=187 or ball.xcor()<=-235:
        
        xSpeed=xSpeed*-1
        if infinit==0:
            xSpeed=xSpeed//1.5
    if infinit==0:
        if ball.ycor()<= -187:
            b=b-1
            if b>>0:
                ySpeed=b
            else:
                break
    else:
        if ball.ycor()<= -187:
            ySpeed=10
    
    x=x+xSpeed
    y=y+ySpeed
    ySpeed=ySpeed-gravity
    



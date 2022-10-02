import turtle
from turtle import*
import random

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

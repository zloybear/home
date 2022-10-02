import turtle
from turtle import*

colors={'red':(1,0,0),'green':(0,1,0),'blue':(0,0,1),'p':(1,0,1)}

while True:
    for i in colors:
        color(colors[i])
        forward(100)
        left(90)
        

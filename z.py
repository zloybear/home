import turtle
from turtle import*

colors={'red':(1,0,0),'green':(0,1,0),'blue':(0,0,1),'p':(1,0,1)}
figutre={'square':90,'triangle':120}
a='square'

while True:
    for i in colors:
        color(colors[i])
        forward(100)
        left(figutre[a])
        

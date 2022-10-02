import turtle
from turtle import*
a=Pen()
a.speed(100)
for i in range(100000):
    col=i%6+1
    if col==1:
        a.color('green')
    elif col==2:
        a.color('blue')
    elif col==3:
        a.color('orange')
    elif col==4:
        a.color('purple')
    elif col==5:
        a.color('dark blue')
    elif col==2:
        a.color('pink')
    a.circle((i+1)*1)
    a.left(60)
    

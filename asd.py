import turtle
from turtle import*
def drawe(obect,size,colorq):
    color(colorq)
    begin_fill()
    if obect=='thiangle':
        for i in range(3):
            forward(size)
            left(120)
    if obect=='square':
        for i in range(4):
            forward(size)
            left(90)
    if obect=='circle':
        circle(size)
    end_fill()


    
drawe('circle',150,'cyan')

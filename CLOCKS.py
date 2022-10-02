from turtle import *
import time
h=0
m=0
s=0
tracer(False)
def draw_dial():
    up()
    for i in range(60):
        forward(100)
        dot(4)
        if i%5==0:
            down()
            pensize(5)
            forward(20)
            left(180)
            forward(20)
            left(180)
            up()
        left(180)
        forward(100)
        left(180)
        right(6)
def make_arrow(lenght,color,name):
    s=Shape('compound')
    poly=((0,0),(0,lenght),(4,lenght-5),(0,lenght+6),(-4,lenght-5),(0,lenght))
    s.addcomponent(poly,color,color)
    register_shape(name,s)

draw_dial()
tracer(True)
color('white')

Sek=Pen()
make_arrow(80,'red','sek')
Sek.shape('sek')
Sek.left(90)
Min=Pen()
make_arrow(90,'blue','min')
Min.shape('min')
Min.left(90)
Hour=Pen()
make_arrow(60,'green1','hour')
Hour.shape('hour')
Hour.left(90)

while True:
    for i in range(12):
        for i in range(60):
            for i in range(60):
                time.sleep(1)
                Sek.right(6)
            Min.right(6)
        Hour.right(30)
    
        
    



        



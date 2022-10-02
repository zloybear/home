import turtle
import time
from turtle import*
pen=Pen()
speed(0)
def kyb():
    skin1=Shape('compound')
    poly=((0,0),(0,15),(15,15),(15,0),(0,0))
    skin1.addcomponent(poly,'cyan','gray')
    register_shape('kyd',skin1)
    return 'kyd'
def listo(n):
    dancers=[]
    for i in range(n):
        pen.up()
        pen.forward(10)
        pen.left(360/n)
        update()
        dancers.append(pen.clone())
    return dancers
def cooldance(list1):
    while True:
        for i in list1:
            i.forward(10)
            i.left(10)
            i.forward(10)
            i.right(20)
        update()
        time.sleep(0.01)
tracer(False)
pen.shape(kyb())
cooldance(listo(55))



    

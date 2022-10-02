import turtle
from turtle import*
import datetime
from datetime import*
pen=turtle.Pen()
def jump(distance,angle=0):
    up()
    left(angle)
    forward(distance)
    right(angle)
    down()
    
def dial(radius):
    reset()
    pensize(5)
    down()
    color('black')
    for i in range(60):
        jump(radius)
        if i %5==0:
            forward(10)
            jump((radius+10)*-1)
        else:
            turtle.dot(6)
            jump((radius)*-1)
        right(6)
        
def arrow(dlina,tr):
    reset()
    down()
    pensize(6)
    forward(dlina)
    pensize(5)
    right(150)
    begin_fill()
    for i in range(3):
        forward(tr)
        right(120)
    end_fill()
    up()
    
def make_hand_shape(name,laenge,spitze):
    reset()
    begin_poly()
    arrow(laenge,spitze)
    end_poly()
    form=get_poly()
    register_shape(name,form)
    
def setup():
    global second_arrow,minute_arrow,hour_arrow
    reset()
    make_hand_shape('second',170,10)
    make_hand_shape('minute',120,20)   
    make_hand_shape('hour',70,30)
    second_arrow=Turtle()
    second_arrow.shape('second')
    second_arrow.color('red')
    minute_arrow=Turtle()
    minute_arrow.color('black')
    minute_arrow.shape('minute')
    hour_arrow=Turtle()
    hour_arrow.color('black')
    hour_arrow.shape('hour')
    dial(200)

def tick():
    tracer(True)
    t=datetime.today()
    second_arrow.setheading(180-6*t.second)
    minute_arrow.setheading(180-6*t.minute)
    hour_arrow.setheading(180-30*t.hour-0.5*t.minute)
    return tick()
tracer(False)
setup()
up()
forward(200)
update()
tick()
done()





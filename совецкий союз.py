import turtle
from turtle import*
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
speed(0)
listcolor1=['#119933','#aaaa00','#ff00ff','#dd00aa','#994455','#211355']
star(-200,-200,listcolor1)

import turtle
from turtle import*
def kyb():
    skin1=Shape('compound')
    poly=((0,0),(0,15),(15,15),(15,0),(0,0))
    skin1.addcomponent(poly,'cyan','gray')
    register_shape('kyd',skin1)
    return 'kyd'
shape(kyb())
color('pale green')
for i in range(6):
    forward(100)
    left(60)



    

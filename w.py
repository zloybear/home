import turtle
from turtle import*
colors=['navy','purple','maroon','blue','purple1','green']
speed(100)
for i in range(5000):
    color(colors[i%6])
    forward(i)
    right(152)

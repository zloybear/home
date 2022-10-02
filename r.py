import turtle
from turtle import*
speed(100)
angles=[30,60,80,70,55]
colors=['navy','purple','maroon','blue','purple1','green','red4']
for i in range(5000):
    if i%2:
        angles.reverse()
    if i%100:
        angles.sort()
    color(colors[i%7])
    forward(i/2)
    right(angles[i%5])

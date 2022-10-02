import turtle
from turtle import*
speed(100)
angles=[30,60,80,70,55]
colors=[(0.2,0.5,1),(1,0.7,0),(1,1,0),(0,1,0.5),(0,0,1)]
for i in range(5000):
    if i%2:
        angles.reverse()
    if i%100:
        angles.sort()
    color(colors[i%4])
    forward(i/2)
    right(angles[i%5])

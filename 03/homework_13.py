#Colorful firework 
from turtle import forward, bgcolor, exitonclick, shape, speed, setpos, penup, pendown, pencolor, goto, left
from random import randint, choice

shape()
speed(0)
bgcolor('black')
colors = ['blue','red','green','yellow','white','purple','pink']

for i in range(20):
    penup()
    goto(randint(-500,500),randint(-300,300))
    pendown()
    distance = randint(20,200)
    pencolor(choice(colors))
    for j in range(36):
        forward(distance)
        left(170)

exitonclick()
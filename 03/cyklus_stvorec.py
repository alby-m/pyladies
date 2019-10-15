from turtle import forward,  left, right, exitonclick, shape, penup, pendown, speed
shape()
speed(0)

left(90)
penup()
forward(150)
pendown()
right(90)
#moving the origin up

for i in range(18):
    for j in range(4):
        forward(50)
        left(90)
    left(20)

right(90) 
forward(100)
left(90)

for i in range(12):
    for j in range (2):
        left(j*120)
        #in first cycle it will not affect it, in the second it will multiply it by 1 so it will turn
        for k in range (60):
             left(1)
             forward((i/5)+0.5)
    left(30+(225*(i%2)))
    #turning it down so it will continue in drawing the stem, it is differentiated by modulo so after every second leaf it will turn by dirrent angle
    forward(25)
    left(225-(135*(i%2)))
    #turning the arrow so it will draw every second leaf under different angle

exitonclick()
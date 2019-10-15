from turtle import forward, left, right, exitonclick, shape, penup, pendown
shape('turtle')

for i in range (10):
    forward(10+5*i)
    penup()
    forward(5)
    pendown()

exitonclick()
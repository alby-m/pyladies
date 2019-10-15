from turtle import forward, shape, left, right, exitonclick 
shape('turtle')

diagonal = ((2**(1/2))*30)

for i in range(10):
    forward(30)
    left(90)
    forward(30)
    left(90)
    forward(30)
    right(135)
    forward(diagonal/2)
    right(90)
    forward(diagonal/2)
    right(90)
    forward(diagonal)
    right(135)
    forward(30)
    right(135)
    forward(diagonal)
    left(45)
    forward(3)

exitonclick()

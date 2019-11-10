from turtle import forward, left, right, exitonclick, shape
shape('turtle')

def house(size):
    diagonal = ((2**(1/2))*size)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    right(135)
    forward(diagonal/2)
    right(90)
    forward(diagonal/2)
    right(90)
    forward(diagonal)
    right(135)
    forward(size)
    right(135)
    forward(diagonal)
    left(45)
    forward(size)

for i in range(4):
    house(i*10+10)

exitonclick()
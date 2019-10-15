from turtle import shape, left, forward, exitonclick
shape()
n = 0
#x = 0

#for i in range(80):
#    left(30)
#    forward(n+x)
#    x = x + 2*n

for i in range(1000):
    left(5)
    forward(n+(i/100))

exitonclick()

from turtle import forward, left, exitonclick, shape
shape()

n = int(input("Select n:"))

for i in range(200):
    forward(n+i*n)
    left(180-(180*(1-(2/(20*(1+i)))))) 

exitonclick()
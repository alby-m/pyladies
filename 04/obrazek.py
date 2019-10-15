from turtle import forward, left, right, getcanvas

forward(50)
left(60)
forward(50)
right(60)
forward(50)

getcanvas().postscript(file='obrazek.ps')
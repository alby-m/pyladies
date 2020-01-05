import matplotlib.pyplot as plt
import numpy

ax = plt.gca()
plt.axis('square')
ax.set_xticks(numpy.arange(-100, 125, 25))
ax.set_yticks(numpy.arange(-100, 125, 25))
ax.tick_params(axis='both', which='major', labelsize=5)
plt.grid(True)
fuel = plt.Circle((30, 25), 2.9925)
x1 = numpy.linspace(25.23,49.77,100)
y1 = -1*x1+75
plt.plot(x1, y1, '-r')
x2 = numpy.linspace(25.23,49.77,100)
y2 = x2-75
plt.plot(x2, y2, '-r')
x3 = numpy.linspace(-49.77,-25.23,100)
y3 = -1*x3-75
plt.plot(x3, y3, '-r')
x4 = numpy.linspace(-49.77,-25.23,100)
y4 = x4+75
plt.plot(x4, y4, '-r')
y5 = numpy.linspace(-25.23,25.23,100)
x5 = 49.77-0*y5
plt.plot(x5, y5, '-r')
y6 = numpy.linspace(-25.23,25.23,100)
x6 = -49.77-0*y6
plt.plot(x6, y6, '-r')
x7 = numpy.linspace(-25.23,25.23,100)
y7 = 49.77-0*x7
plt.plot(x7, y7, '-r')
x8 = numpy.linspace(-25.23,25.23,100)
y8 = -49.77-0*x8
plt.plot(x8, y8, '-r')

x11 = numpy.linspace(37.22,87.78,100)
y11 = -1*x11+125
plt.plot(x11, y11, '-g')
x12 = numpy.linspace(37.22,87.78,100)
y12 = x12-125
plt.plot(x12, y12, '-g')
x13 = numpy.linspace(-87.78,-37.22,100)
y13 = -1*x13-125
plt.plot(x13, y13, '-g')
x14 = numpy.linspace(-87.78,-37.22,100)
y14 = x14+125
plt.plot(x14, y14, '-g')
y15 = numpy.linspace(-37.22,37.22,100)
x15 = 87.78-0*y15
plt.plot(x15, y15, '-g')
y16 = numpy.linspace(-37.22,37.22,100)
x16 = -87.78-0*y16
plt.plot(x16, y16, '-g')
x17 = numpy.linspace(-37.22,37.22,100)
y17 = 87.78-0*x17
plt.plot(x17, y17, '-g')
x18 = numpy.linspace(-37.22,37.22,100)
y18 = -87.78-0*x18
plt.plot(x18, y18, '-g')
ax.add_artist(fuel)
plt.show()

from matplotlib.pyplot import axis, gca, Circle, grid, plot, show
from numpy import linspace, arange

class Vizualization():

    def plotting(self):
        self.background()
        self.fuel(x,y,r)
        return show()


    def background(self):
        ax = gca()
        axis('square')
        ax.set_xticks(arange(-100, 125, 25))
        ax.set_yticks(arange(-100, 125, 25))
        ax.tick_params(axis='both', which='major', labelsize=5)
        grid(True)

    def fuel(self, x, y, r):
        for f in Extract.get_coordinates

        for f in Fuel_elimination.evaluate():
            fuel = Circle((x, y), r)
            return fuel

        
graph = Vizualization()
graph.plotting()

# ax = gca()
# axis('square')
# ax.set_xticks(arange(-100, 125, 25))
# ax.set_yticks(arange(-100, 125, 25))
# ax.tick_params(axis='both', which='major', labelsize=5)
# grid(True)
# fuel = Circle((-26, 51), 2.9925)
# x1 = linspace(25.23,49.77,100)
# y1 = -1*x1+75
# plot(x1, y1, '-r')
# x2 = linspace(25.23,49.77,100)
# y2 = x2-75
# plot(x2, y2, '-r')
# x3 = linspace(-49.77,-25.23,100)
# y3 = -1*x3-75
# plot(x3, y3, '-r')
# x4 = linspace(-49.77,-25.23,100)
# y4 = x4+75
# plot(x4, y4, '-r')
# y5 = linspace(-25.23,25.23,100)
# x5 = 49.77-0*y5
# plot(x5, y5, '-r')
# y6 = linspace(-25.23,25.23,100)
# x6 = -49.77-0*y6
# plot(x6, y6, '-r')
# x7 = linspace(-25.23,25.23,100)
# y7 = 49.77-0*x7
# plot(x7, y7, '-r')
# x8 = linspace(-25.23,25.23,100)
# y8 = -49.77-0*x8
# plot(x8, y8, '-r')

# x11 = linspace(37.22,87.78,100)
# y11 = -1*x11+125
# plot(x11, y11, '-g')
# x12 = linspace(37.22,87.78,100)
# y12 = x12-125
# plot(x12, y12, '-g')
# x13 = linspace(-87.78,-37.22,100)
# y13 = -1*x13-125
# plot(x13, y13, '-g')
# x14 = linspace(-87.78,-37.22,100)
# y14 = x14+125
# plot(x14, y14, '-g')
# y15 = linspace(-37.22,37.22,100)
# x15 = 87.78-0*y15
# plot(x15, y15, '-g')
# y16 = linspace(-37.22,37.22,100)
# x16 = -87.78-0*y16
# plot(x16, y16, '-g')
# x17 = linspace(-37.22,37.22,100)
# y17 = 87.78-0*x17
# plot(x17, y17, '-g')
# x18 = linspace(-37.22,37.22,100)
# y18 = -87.78-0*x18
# plot(x18, y18, '-g')
# ax.add_artist(fuel)
# show()

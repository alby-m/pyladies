from matplotlib.pyplot import axis, gca, Circle, grid, plot, show, savefig, clf
from numpy import linspace, arange

class Vizualization():
    def __init__(self, fuel_elimination, fuel_data, fuel_tank):
        self.fuel_elimination = fuel_elimination
        self.fuel_data = fuel_data
        self.fuel_tank = fuel_tank

    def plotting(self):
        self.background()
        self.half_circles(self.fuel_tank.circle_1)
        self.half_circles(self.fuel_tank.circle_2)
        self.half_circles(self.fuel_tank.circle_3)
        self.half_circles(self.fuel_tank.circle_4)
        self.half_circles(self.fuel_tank.circle_5)
        self.half_circles(self.fuel_tank.circle_6)
        self.half_circles(self.fuel_tank.circle_7)
        self.half_circles(self.fuel_tank.circle_8)
        self.half_circles(self.fuel_tank.circle_0)
        self.octagon_lines(self.fuel_tank.octagon_i)
        self.octagon_lines(self.fuel_tank.octagon_o)
        self.fuel_cells('IN', 'green')
        savefig('in.svg')
        savefig('in.png')
        clf()
        self.background()
        self.half_circles(self.fuel_tank.circle_1)
        self.half_circles(self.fuel_tank.circle_2)
        self.half_circles(self.fuel_tank.circle_3)
        self.half_circles(self.fuel_tank.circle_4)
        self.half_circles(self.fuel_tank.circle_5)
        self.half_circles(self.fuel_tank.circle_6)
        self.half_circles(self.fuel_tank.circle_7)
        self.half_circles(self.fuel_tank.circle_8)
        self.half_circles(self.fuel_tank.circle_0)
        self.octagon_lines(self.fuel_tank.octagon_i)
        self.octagon_lines(self.fuel_tank.octagon_o)        
        self.fuel_cells('OUT', 'red')
        savefig('out.svg')
        savefig('out.png')

    def octagon_lines(self, octagon):
        x1 = linspace(octagon.intercept-octagon.size,octagon.size,100)
        y1 = -1*x1+octagon.intercept
        plot(x1, y1, color = 'black')
        x2 = linspace(octagon.intercept-octagon.size,octagon.size,100)
        y2 = x2-octagon.intercept
        plot(x2, y2, color = 'black')
        x3 = linspace(-1*octagon.size,octagon.size-octagon.intercept,100)
        y3 = -1*x3-octagon.intercept
        plot(x3, y3, color = 'black')
        x4 = linspace(-1*octagon.size,octagon.size-octagon.intercept,100)
        y4 = x4+octagon.intercept
        plot(x4, y4, color = 'black')
        y5 = linspace(octagon.size-octagon.intercept,octagon.intercept-octagon.size,100)
        x5 = octagon.size-0*y5
        plot(x5, y5, color = 'black')
        y6 = linspace(octagon.size-octagon.intercept,octagon.intercept-octagon.size,100)
        x6 = -1*octagon.size-0*y6
        plot(x6, y6, color = 'black')
        x7 = linspace(octagon.size-octagon.intercept,octagon.intercept-octagon.size,100)
        y7 = octagon.size-0*x7
        plot(x7, y7, color = 'black')
        x8 = linspace(octagon.size-octagon.intercept,octagon.intercept-octagon.size,100)
        y8 = -octagon.size-0*x8
        plot(x8, y8, color = 'black')

    def half_circles(self, half_circle):
        ax = gca()
        border_circle = Circle((half_circle.pos_x, half_circle.pos_y), half_circle.radius, fc='none', ec='black')
        ax.add_artist(border_circle)


    def background(self):
        ax = gca()
        axis('square')
        ax.set_xticks(arange(-100, 125, 25))
        ax.set_yticks(arange(-100, 125, 25))
        ax.tick_params(axis='both', which='major', labelsize=5)
        grid(True)


    def fuel_cells(self, status, fill_color):
        ax = gca()
        for f in self.fuel_elimination.evaluate():
            viz_x = f['coord_x']
            viz_y = f['coord_y']
            viz_r = f['coord_r']
            if f['result'] == status:
                fuel = Circle((viz_x, viz_y), viz_r, color=fill_color)
                ax.add_artist(fuel)

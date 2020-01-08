import matplotlib.pyplot as plt
import numpy

class Fuel_elimination():
    def __init__(self, fuel_tank, fuel_data):
        self.fuel_tank = fuel_tank
        self.fuel_data = fuel_data

    def evaluate(self):
        xyr = self.fuel_data.get_coordinates()
        for i in xyr:
            x = i[0]
            y = i[1]
            r = i[2]
        print(results)

class Extract:
    def get_data(self):
        with open('coordinates.inp', 'r') as file_:
            data = []
            for line in file_:
                data.append(line)
            file_.close()
        return(data)

    def get_coordinates(self):
        coordinates_num = []
        for data_line in self.get_data():
            x = data_line[0:12]
            x = float(x.lstrip())
            y = data_line[13:25]
            y = float(y.lstrip())
            r = float(data_line[39:50])
            coordinate = []
            coordinate.append(x)
            coordinate.append(y)
            coordinate.append(r)
            lst = list(coordinate)
            coordinates_num.append(lst)
        return(coordinates_num)


class Fuel_tank():
    def __init__(self):
        self.octagon_i = Octagon(49.77, 75)
        self.octagon_o = Octagon(87.78, 125)
    
    def in_out_t(self, x, y, r):
        if self.octagon_o.in_out(x,y,r) == 'IN' and self.octagon_i.in_out(x,y,r) == 'OUT':
            print('IN')
        else:
            print('OUT')

class Octagon():
    def __init__(self, size, intercept):
        self.size = size
        self.intercept = intercept
        # self.f1 = -x-y+intercept
        # self.f2 = x-y-intercept
        # self.f3 = -x-y-intercept
        # self.f4 = x-y+intercept

    def in_out(self, x, y, r):
            p = numpy.array([x,y])
            a1 = numpy.array([self.intercept-self.size, self.size])
            b1 = numpy.array([self.size, self.intercept-self.size])
            a2 = numpy.array([self.size, self.size-self.intercept])
            b2 = numpy.array([self.intercept-self.size, -1*self.size])
            a3 = numpy.array([self.size-self.intercept, -1*self.size])
            b3 = numpy.array([-1*self.size, self.size-self.intercept])
            a4 = numpy.array([-1*self.size, self.intercept-self.size])
            b4 = numpy.array([self.size-self.intercept, self.size])
            dist_f1 = abs((-1*x + -1*y + self.intercept)/ (2**(1/2)))
            dist_f2 = abs(( 1*x + -1*y - self.intercept)/ (2**(1/2)))
            dist_f3 = abs((-1*x + -1*y - self.intercept)/ (2**(1/2)))
            dist_f4 = abs(( 1*x + -1*y + self.intercept)/ (2**(1/2)))
            dist_h1 = abs( 1*self.size - y)
            dist_h2 = abs(-1*self.size - y)
            dist_v1 = abs( 1*self.size - x)
            dist_v2 = abs(-1*self.size - x)        
            if  (
                    -1*self.size < x < self.size and -1*self.size < y < self.size and
                    #comparing fuel coordinates with vertical and horizontal borders of octagon
                    numpy.cross(p-a1, b1-a1) > 0 and numpy.cross(p-a2, b2-a2) > 0 and numpy.cross(p-a3, b3-a3) > 0 and numpy.cross(p-a4, b4-a4) > 0
                    #comparing fuel coordinates with diagonal borders of octagon
                ):
                if r > dist_f1 and r > dist_f2 and r > dist_f3 and r > dist_f4 and r > dist_h1 and r > dist_h2 and r > dist_v1 and r > dist_v2:
                #comparing radius with distance between fuel coordinates and borders of octagon
                    return 'BORDER'
                else:
                    return 'IN'
            else:
                if  (
                        ((r+self.size) > abs(x) and self.size-self.intercept < y < self.intercept-self.size) or
                        ((r+self.size) > abs(y) and self.size-self.intercept < x < self.intercept-self.size) or
                        (r > dist_f1 or r > dist_f2 or r > dist_f3 or r > dist_f4) and
                        -1*self.size < x < self.size and -1*self.size < y < self.size
                    ):
                        return 'BORDER'
                else:
                    return 'OUT'

# class Circle():
#     def __init__(self, pos_x, pos_y, radius):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.radius = radius

fuel_tank_0 = Fuel_tank()
fuel_tank_0.in_out_t(-26, 51, 2.9925)
# input_data = Extract()
# output = Fuel_elimination(fuel_tank_0, input_data)


# output.evaluate()
# octagon_i = Octagon(49.77, 75)
# octagon_o = Octagon(87.78, 125)
# octagon_o.in_out(42, 80, 2.9925)

# output = Extract()
# output.get_coordinates()

# class Vizualization():
#     def grid(self):
#         ax = plt.gca()
#         ax.set_xticks(numpy.arange(-250, 250, 25))
#         ax.set_yticks(numpy.arange(-250, 250, 25))
#         ax.tick_params(axis='both', which='major', labelsize=5)
#         plt.axis('square')
#         plt.grid(True)
#         fuel = plt.Circle(output.get_coordinates()[0], output.get_coordinates()[1], output.get_coordinates()[2])
#         ax.add_artist(fuel)
#         plt.show()


# ax = plt.gca()
# ax.set_xticks(numpy.arange(-250, 250, 25))
# ax.set_yticks(numpy.arange(-250, 250, 25))
# ax.tick_params(axis='both', which='major', labelsize=5)
# plt.axis('square')
# plt.grid(True)
# fuel = plt.Circle((x, y), r)
# ax.add_artist(fuel)

# plt.show()        

# # class Drawing_fuel(Vizualization):
# #     def inside(self):
# #         print(fuel)
# #         # ax.add_artist(fuel)
# #         # plt.show()

# plot = Vizualization()
# plot.grid()


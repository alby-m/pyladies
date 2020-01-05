import matplotlib.pyplot as plt
import numpy

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

    def __init__(self, octagon, circle):
        self.octagon = octagon
        self.circle = circle

class Octagon():
    def make_octagon(self, size, intercept):
        x_axis = size
        y_axis = size
        f1 = -x-y+intercept
        f2 = x-y-intercept
        f3 = -x-y-intercept
        f4 = x-y+intercept
        return()

class Circle():
    def make_circle(self, pos_x, pos_y, radius):
        


# fuel_tank = Fuel_tank()
inner_octagon = Octagon()
inner_octagon.make_octagon(49.77, 75)
outer_octagon = Octagon()
outer_octagon.make_octagon(87.78, 125)




output = Extract()
output.get_coordinates()






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


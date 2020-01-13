from numpy import arccos, array, dot, pi, cross, linspace, arange
from numpy.linalg import det, norm
from matplotlib.pyplot import axis, gca, Circle, grid, plot, show

class Fuel_elimination():
    def __init__(self, fuel_tank, fuel_data):
        self.fuel_tank = fuel_tank
        self.fuel_data = fuel_data

    def evaluate(self):
        xyr = self.fuel_data.get_coordinates()
        raw = self.fuel_data.get_data()
        result_list = []
        for i in range(len(xyr)):
            x = xyr[i][0]
            y = xyr[i][1]
            r = xyr[i][2]
            processed_row = {}
            processed_row['result'] = (self.fuel_tank.in_out(x, y, r))
            processed_row['coord_x'] = x
            processed_row['coord_y'] = y
            processed_row['coord_r'] = r
            processed_row['raw_data'] = raw[i]
            result_list.append(processed_row)
        return(result_list)

    def separate(self):
        with open('coordinate_file.inp', 'w') as file_in:
            for row in self.evaluate():
                if row['result'] == 'IN':
                    file_in.write(str(row['raw_data']))
            file_in.close()

class Extract:
    def get_data(self):
        with open('coordinates_all.inp', 'r') as file_:
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
    
    def in_out(self, x, y, r):
        if self.octagon_o.in_out_border(x,y,r) == 'IN' and self.octagon_i.in_out_border(x,y,r) == 'OUT':
            return 'IN'
        else:
            return 'OUT'

class Octagon():
    def __init__(self, size, intercept):
        self.size = size
        self.intercept = intercept

    def in_out_border(self, x, y, r):
            p = array([x,y])
            a1 = array([self.intercept-self.size, self.size])
            a2 = array([self.size, self.intercept-self.size])
            a3 = array([self.size, self.size-self.intercept])
            a4 = array([self.intercept-self.size, -1*self.size])
            a5 = array([self.size-self.intercept, -1*self.size])
            a6 = array([-1*self.size, self.size-self.intercept])
            a7 = array([-1*self.size, self.intercept-self.size])
            a8 = array([self.size-self.intercept, self.size])
            oct_pts = [a1, a2, a3, a4, a5, a6, a7, a8]
            for oct_pt in range(7):
                if all(oct_pts[oct_pt] == p) or all(oct_pts[(oct_pt+1)%8] == p):
                    distance = 0
                elif arccos(dot((p - oct_pts[oct_pt]) / norm(p - oct_pts[oct_pt]), (oct_pts[(oct_pt+1)%8] - oct_pts[oct_pt]) / norm(oct_pts[(oct_pt+1)%8] - oct_pts[oct_pt]))) > pi / 2:
                    distance = norm(p - oct_pts[oct_pt])
                elif arccos(dot((p - oct_pts[(oct_pt+1)%8]) / norm(p - oct_pts[(oct_pt+1)%8]), (oct_pts[oct_pt] - oct_pts[(oct_pt+1)%8]) / norm(oct_pts[oct_pt] - oct_pts[(oct_pt+1)%8]))) > pi / 2:
                    distance = norm(p - oct_pts[(oct_pt+1)%8])
                else:
                    distance = norm(cross(oct_pts[oct_pt]-oct_pts[(oct_pt+1)%8], oct_pts[oct_pt]-p))/norm(oct_pts[(oct_pt+1)%8]-oct_pts[oct_pt])
                if abs(distance) < r:
                    return 'BORDER'
            if  (
                    -1*self.size < x < self.size and -1*self.size < y < self.size and
                    #comparing fuel coordinates with vertical and horizontal borders of octagon
                    cross(p-a1, a2-a1) > 0 and cross(p-a3, a4-a3) > 0 and cross(p-a5, a6-a5) > 0 and cross(p-a7, a8-a7) > 0
                    #comparing fuel coordinates with diagonal borders of octagon
                ):
                return 'IN'
            else:
                return 'OUT'

# class Circle():
#     def __init__(self, pos_x, pos_y, radius):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.radius = radius

class Vizualization():
    def __init__(self, fuel_elimination, fuel_data):
        self.fuel_elimination = fuel_elimination
        self.fuel_data = fuel_data

    def plotting(self):
        self.background()
        self.fuel_cells()
        show()


    def background(self):
        ax = gca()
        axis('square')
        ax.set_xticks(arange(-100, 125, 25))
        ax.set_yticks(arange(-100, 125, 25))
        ax.tick_params(axis='both', which='major', labelsize=5)
        grid(True)


    def fuel_cells(self):
        ax = gca()
        for f in self.fuel_elimination.evaluate():
            viz_x = f['coord_x']
            viz_y = f['coord_y']
            viz_r = f['coord_r']
            if f['result'] == 'IN':
                fuel = Circle((viz_x, viz_y), viz_r, color='green')
            # else:
            #     fuel = Circle((viz_x, viz_y), viz_r, color='red')
                ax.add_artist(fuel)


fuel_tank = Fuel_tank()
input_data = Extract()
output = Fuel_elimination(fuel_tank, input_data)
# output.evaluate()
# output.separate()
graph = Vizualization(output, input_data)
graph.plotting()



from numpy import arccos, array, dot, pi, cross, linspace, arange
from numpy.linalg import det, norm
from matplotlib.pyplot import axis, gca, Circle, grid, plot, show

class Fuel_elimination():
    def __init__(self, fuel_tank, fuel_data):
        self.fuel_tank = fuel_tank
        self.fuel_data = fuel_data

    def evaluate(self):
        #saving list of data with fuel coordinates into variable
        xyr = self.fuel_data.get_coordinates()
        #saving raw data into variable
        raw = self.fuel_data.get_data()
        result_list = []
        #creating dictionary consisiting of resulting position, coordinates and originate line
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

    def separate(self, file_name, status):
        #new file creation with only lines correspondinf to selected position 
        with open(file_name, 'w') as file_sep:
            for row in self.evaluate():
                if row['result'] == status:
                    file_sep.write(str(row['raw_data']))
            file_in.close()

class Extract:
    #opening the source file, extracting the data and saving them into variable
    def get_data(self):
        with open('coordinates_all.inp', 'r') as file_:
            data = []
            for line in file_:
                data.append(line)
            file_.close()
        return(data)

    def get_coordinates(self):
        #processing the source data into simple numbers representing coordinates
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
        #fuel inside of the outside octagon belong inside the fuel tank, since fuel inside of the inside octagon needs to be removed
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
            for oct_pt in range(8):
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
    def __init__(self, fuel_elimination, fuel_data, fuel_tank):
        self.fuel_elimination = fuel_elimination
        self.fuel_data = fuel_data
        self.fuel_tank = fuel_tank

    def plotting(self):
        self.background()
        self.octagon_lines(self.fuel_tank.octagon_i)
        self.octagon_lines(self.fuel_tank.octagon_o)
        self.fuel_cells()
        show()

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
# output.separate('coordinate_file.inp', 'IN')
graph = Vizualization(output, input_data, fuel_tank)
graph.plotting()



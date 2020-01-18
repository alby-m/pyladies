import octagon_class, circle_tank_class

class Fuel_tank():
    def __init__(self):
        self.octagon_i = octagon_class.Octagon(49.77, 75)
        # self.octagon_i = octagon_class.Octagon(30, 45)
        self.octagon_o = octagon_class.Octagon(87.78, 125)
        self.circle_1 = circle_tank_class.Circle_tank(50, 75, 5.70575)
        self.circle_2 = circle_tank_class.Circle_tank(75, 50, 5.70575)
        self.circle_3 = circle_tank_class.Circle_tank(75, -50, 5.70575)
        self.circle_4 = circle_tank_class.Circle_tank(50, -75, 5.70575)
        self.circle_5 = circle_tank_class.Circle_tank(-50, -75, 5.70575)
        self.circle_6 = circle_tank_class.Circle_tank(-75, -50, 5.70575)
        self.circle_7 = circle_tank_class.Circle_tank(-75, 50, 5.70575)
        self.circle_8 = circle_tank_class.Circle_tank(-50, 75, 5.70575)
        self.circle_0 = circle_tank_class.Circle_tank(0, 75.26, 5.25)


    def in_out(self, x, y, r):
        #fuel inside of the outside octagon belong inside the fuel tank, while fuel inside of the inside octagon needs to be removed
        if  (
                (self.octagon_o.in_out_border(x,y,r) == 'IN' or 
                self.circle_1.in_out_border(x, y, r) == 'IN' or
                self.circle_2.in_out_border(x, y, r) == 'IN' or 
                self.circle_3.in_out_border(x, y, r) == 'IN' or
                self.circle_4.in_out_border(x, y, r) == 'IN' or
                self.circle_5.in_out_border(x, y, r) == 'IN' or
                self.circle_6.in_out_border(x, y, r) == 'IN' or
                self.circle_7.in_out_border(x, y, r) == 'IN' or
                self.circle_8.in_out_border(x, y, r) == 'IN')
                and self.octagon_i.in_out_border(x,y,r) == 'OUT' and self.circle_0.in_out_border(x, y, r) == 'OUT'
            ):
            return 'IN'
        else:
            return 'OUT'
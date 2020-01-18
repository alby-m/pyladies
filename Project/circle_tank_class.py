class Circle_tank():
    def __init__(self, pos_x, pos_y, radius):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius

    def in_out_border(self, x, y, r):
        distance = abs(((self.pos_x-x)**2 +(self.pos_y-y)**2)**(1/2))
        if distance > (r+self.radius):
            return 'OUT'
        elif distance < abs(r-self.radius):
            return 'IN'
        else:
            return 'BORDER'
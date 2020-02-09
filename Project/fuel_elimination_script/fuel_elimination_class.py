class Fuel_elimination():
    def __init__(self, fuel_tank, fuel_data):
        self.fuel_tank = fuel_tank
        self.fuel_data = fuel_data
        self.result_list = []

    def evaluate(self):
        if len(self.result_list) != 0:
            return(self.result_list)
        #saving list of data with fuel coordinates into variable
        xyr = self.fuel_data.get_coordinates()
        #saving raw data into variable
        raw = self.fuel_data.get_data()
        #creating dictionary consisiting of resulting status IN or OUR, coordinates and originate line
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
            self.result_list.append(processed_row)
            if int((i % ((len(xyr))/20))) == 0 or int(i+1) == len(xyr):
                print('Data evaluation: '+str(round((i/len(xyr))*100))+' percent done.')
        return(self.result_list)

    def separate(self, file_name, status):
        #new file creation with only lines marked with selected status
        print('Writing file for '+status+' coordinates.')
        with open(file_name, 'w') as file_sep:
            for row in self.evaluate():
                if row['result'] == status:
                    file_sep.write(str(row['raw_data']))
            file_sep.close()



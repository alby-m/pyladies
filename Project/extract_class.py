class Extract:
    def __init__(self, source):
        self.source = source

    #opening the source file, extracting the data and saving them into variable
    def get_data(self):
        with open(self.source, 'r') as file_:
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
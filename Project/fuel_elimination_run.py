import fuel_tank_class, fuel_elimination_class, vizualization_class, circle_tank_class, extract_class

fuel_tank = fuel_tank_class.Fuel_tank()
input_data = extract_class.Extract('coordinates_all.inp')
output = fuel_elimination_class.Fuel_elimination(fuel_tank, input_data)
output.separate('coordinate_file_o.inp', 'OUT')
graph = vizualization_class.Vizualization(output, input_data, fuel_tank)
# graph.plotting()

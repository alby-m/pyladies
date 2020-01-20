import fuel_tank_class, fuel_elimination_class, vizualization_class, circle_tank_class, extract_class
import uuid
import os

while True:
    #user chooses the path to the source file
    coordinates = input('Enter the filename:')
    if os.path.exists(coordinates):
        break
    else:
        print('File does not exist, try again.')

output_file_name = input('Select the output filename:')
#in case user will not type any particular output file name, unique name will be automatically generated
if len(output_file_name) == 0:
    output_file_name = str(uuid.uuid4())

fuel_tank = fuel_tank_class.Fuel_tank()
input_data = extract_class.Extract(coordinates)
output = fuel_elimination_class.Fuel_elimination(fuel_tank, input_data)

while True:
    #user chooses which cells he wants to generate file for, in case he does not make a selection, program will generate files for both, IN and OUT cells
    output_type = input('Select which cell coordinates you require to generate into file- IN/OUT/BOTH (Default will generate both files):')
    if output_type == 'IN':
        output.separate(output_file_name+'.inp', output_type)
        break
    elif output_type == 'OUT':
        output.separate(output_file_name+'.inp', output_type)
        break
    elif len(output_type) == 0:
        output.separate(output_file_name+'_in.inp', 'IN')
        output.separate(output_file_name+'_out.inp', 'OUT')
        break
    elif output_type == 'BOTH':
        output.separate(output_file_name+'_in.inp', 'IN')
        output.separate(output_file_name+'_out.inp', 'OUT')
        break
    else:
        print('Your selection is not valid.')

graph = vizualization_class.Vizualization(output, input_data, fuel_tank)
graph.plotting()

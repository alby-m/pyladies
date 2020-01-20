import fuel_elimination_class, fuel_tank_class, extract_class
import uuid, os

def create_file(filename):
    with open(filename, mode ='w+') as _file:
        _file.write("-4.85700E+01 -6.06252E+01  7.46856E+01 2.99250E+00 222 \n")
        _file.write(" 7.49443E+01 -4.25067E+01  1.35353E+02 2.99250E+00 222 \n")
        _file.write(" 3.75672E+01 -4.12563E+01  2.07124E+02 2.99250E+00 222 \n")
        _file.write("-6.42121E+01 -2.24541E+01  1.24260E+02 2.99250E+00 222 \n")
        _file.write(" 5.24217E+01 -8.15911E+01  7.61183E+01 2.99250E+00 222 \n")
        _file.write(" 4.20057E+01 -3.66959E+01  6.87857E+01 2.99250E+00 222 \n")
        _file.write("-3.93579E+01 -2.08827E+01  1.27062E+02 2.99250E+00 222 \n")
        _file.write("-1.17074E+01  3.71974E+01  2.41426E+02 2.99250E+00 222 \n")
        _file.write("-4.49644E+01  2.92322E+00  2.47581E+02 2.99250E+00 222 \n")
        _file.write("-1.83827E+01 -3.93507E+01  1.01622E+02 2.99250E+00 222 \n")
        _file.close()

def remove_file(filename):
    os.remove(filename)

def test_evaluate():
    filename = str(uuid.uuid4())+".txt"
    create_file(filename)
    fuel_tank = fuel_tank_class.Fuel_tank()
    fuel_data = extract_class.Extract(filename)
    output_t = fuel_elimination_class.Fuel_elimination(fuel_tank, fuel_data)
    test_evaluation = output_t.evaluate()
    assert len(test_evaluation) > 0
    assert len(test_evaluation) == 10
    assert test_evaluation[1]['coord_r'] == 2.9925
    assert test_evaluation[0]['result'] == 'IN'
    assert test_evaluation[4]['coord_x'] == 52.4217
    assert test_evaluation[9]['coord_y'] == -39.3507
    assert '222' in test_evaluation[5]['raw_data']
    remove_file(filename)

def test_separate():
    filename = str(uuid.uuid4())+".txt"
    create_file(filename)
    fuel_tank = fuel_tank_class.Fuel_tank()
    fuel_data = extract_class.Extract(filename)
    output_t = fuel_elimination_class.Fuel_elimination(fuel_tank, fuel_data)
    output_t.separate('output_file_t.txt', 'IN')
    with open('output_file_t.txt', 'r') as file_t:
        data_t = file_t.readlines()
        file_t.close()
    assert len(data_t) == 3
    assert '-2.24541E+01' in data_t[2]
    assert '5.24217E+01' not in data_t
    assert len(data_t[1]) == 56
    remove_file(filename)
    remove_file('output_file_t.txt')

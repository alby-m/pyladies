import extract_class
import os
import uuid

def create_file(created_file_name):
    with open(created_file_name, mode ='w+') as _file:
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

def remove_file(removed_file_name):
    os.remove(removed_file_name)

def test_get_data():
    filename = str(uuid.uuid4())+".txt"
    create_file(filename)
    test_file = extract_class.Extract(filename)
    test_data = test_file.get_data()
    assert len(test_data) > 0
    assert len(test_data) == 10
    assert '2.9925' in test_data[1]
    remove_file(filename)

def test_get_coordinates():
    filename = str(uuid.uuid4())+".txt"
    create_file(filename)
    test_file = extract_class.Extract(filename)
    test_coordinates = test_file.get_coordinates()
    assert len(test_coordinates) > 0
    assert len(test_coordinates) == 10
    assert 222 not in test_coordinates[1]
    assert -48.57 == test_coordinates[0][0]
    remove_file(filename)


import fuel_tank_class

def test_in_out():
    fuel_tank = fuel_tank_class.Fuel_tank()
    assert fuel_tank.in_out(30,30,2) == 'OUT'
    assert fuel_tank.in_out(50,0,2) == 'OUT'
    assert fuel_tank.in_out(120,30,2) == 'OUT'
    assert fuel_tank.in_out(67,40,2) == 'IN'
    assert fuel_tank.in_out(53,20,2) == 'IN'
    assert fuel_tank.in_out(50,75,2) == 'IN'

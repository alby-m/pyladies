import circle_tank_class

def test_in_out_border():
    circle_tank = circle_tank_class.Circle_tank(10,10,5)
    assert circle_tank.in_out_border(20,30,3) == 'OUT'
    assert circle_tank.in_out_border(21,12,5) == 'OUT'
    assert circle_tank.in_out_border(10,19,3) == 'OUT'
    assert circle_tank.in_out_border(10,10,3) == 'IN'
    assert circle_tank.in_out_border(11,11,2) == 'IN'
    assert circle_tank.in_out_border(10,10,3) == 'IN'
    assert circle_tank.in_out_border(18,10,3) == 'BORDER'
    assert circle_tank.in_out_border(10,10,5) == 'BORDER'
    assert circle_tank.in_out_border(12,12,3) == 'BORDER'



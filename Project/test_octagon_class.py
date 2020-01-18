import octagon_class

def test_in_out_border():
    octagon = octagon_class.Octagon(30, 45)
    assert octagon.in_out_border(0,0,3) == 'IN'
    assert octagon.in_out_border(-5,-5,3) == 'IN'
    assert octagon.in_out_border(25,-10,3) == 'IN'
    assert octagon.in_out_border(0,28,3) == 'BORDER'
    assert octagon.in_out_border(-20,-23,3) == 'BORDER'
    assert octagon.in_out_border(27,0,3) == 'BORDER'
    assert octagon.in_out_border(35,0,3) == 'OUT'
    assert octagon.in_out_border(-27,-27,3) == 'OUT'
    assert octagon.in_out_border(33.1,0,3) == 'OUT'

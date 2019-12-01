import piskvorky_classes

def test_take():
    o = piskvorky_classes.Player('o')
    field = o.take(1, '--------------------')
    assert field[1] == 'o'
    assert len(field) == 20
    assert field.count('o') == 1
    assert field.count('-') == 19

def test_player_take():
    x = piskvorky_classes.Pc('x')
    field = x.player_take('-x--o---------------')
    assert len(field) == 20
    assert field.count('x') == 2
    assert field.count('-') == 17
    for i in range(16):
        field = x.player_take(field)
    assert field[4] != 'x'
    assert field[4] == 'o'
    field_long = []
    for i in range(100):
        field_long.append('-')
    field_str = ''.join(field_long)
    for i in range(100):
        field_str = x.player_take(field_str)
    assert field_str.count('-') == 0
    assert field_str.count('x') == 100

def test_evaluate():
    x = piskvorky_classes.Pc('x')
    o = piskvorky_classes.User('o')
    game_1 = piskvorky_classes.Match('-xoxoxoxoxoxoxoxoxox', x, o)
    game_2 = piskvorky_classes.Match('-xxx----------------', x, o)
    game_3 = piskvorky_classes.Match('-ooo----------------', x, o)
    game_4 = piskvorky_classes.Match('xxooxxooxxooxxooxxoo', x, o)
    assert game_1.evaluate() == 0 
    assert game_2.evaluate() == ('"x" has won.')
    assert game_3.evaluate() == ('"o" has won.')
    assert game_4.evaluate() == ('It is a tie.')

def test_digit():
    o = piskvorky_classes.Player('o')
    assert o.digit('3') == True
    assert o.digit('a') == False
    assert o.digit('3a') == False
    assert o.digit('.5') == False
    assert o.digit('0.5') == False

def test_range():
    o = piskvorky_classes.User('o')
    field = ('-xoxoxoxoxoxoxoxoxox')
    assert o.range(19, field) == True
    assert o.range(0, field) == True
    assert o.range(22, field) == False

def test_available():
    o = piskvorky_classes.User('o')
    field = list('-xoxoxoxoxoxoxoxoxo-')
    assert o.available(10,field) == False
    assert o.available(19, field) == True

def test_input_check():
    o = piskvorky_classes.User('o')
    field = list('--oxoxoxoxoxoxoxoxo-')
    assert o.input_check('1', field) == ('ok')
    assert o.input_check('a', field) == ('Select digit')
    assert o.input_check('21', field) == ('Your selected position is not valid, try again.')
    assert o.input_check('5', field) == ('This field is not available, select another one.')
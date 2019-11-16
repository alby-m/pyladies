import ai, piskvorky, util

def test_take():
    field = util.take('--------------------', 1, 'o')
    assert field[1] == 'o'
    assert len(field) == 20
    assert field.count('o') == 1
    assert field.count('-') == 19

def test_pc_take():
    field = ai.pc_take('-x--o---------------', 'x')
    assert len(field) == 20
    assert field.count('x') == 2
    assert field.count('-') == 17
    for i in range(16):
        field = ai.pc_take(field, 'x')
    assert field[4] != 'x'
    assert field[4] == 'o'
    field_long = []
    for i in range(10000):
        field_long.append('-')
    field_str = ''.join(field_long)
    for i in range(10000):
        field_str = ai.pc_take(field_str, 'x')
    assert field_str.count('-') == 0
    assert field_str.count('x') == 10000

def test_evaluate():
    assert piskvorky.evaluate('-xoxoxoxoxoxoxoxoxox') == 0 
    assert piskvorky.evaluate('-xxx----------------') == ('"x" has won.')
    assert piskvorky.evaluate('----ooo-------------') == ('"o" has won.')
    assert piskvorky.evaluate('xxooxxooxxooxxooxxoo') == ('It is a tie.')

def test_digit():
    assert piskvorky.digit('3') == True
    assert piskvorky.digit('a') == False
    assert piskvorky.digit('3a') == False
    assert piskvorky.digit('.5') == False
    assert piskvorky.digit('0.5') == False

def test_range():
    assert piskvorky.range(19) == True
    assert piskvorky.range(0) == True
    assert piskvorky.range(22) == False

def test_available():
    field = list('-xoxoxoxoxoxoxoxoxo-')
    assert piskvorky.available(field, 10) == False
    assert piskvorky.available(field, 19) == True

def test_input_check():
    field = list('--oxoxoxoxoxoxoxoxo-')
    assert piskvorky.input_check(field, '1') == ('ok')
    assert piskvorky.input_check(field, 'a') == ('Select number')
    assert piskvorky.input_check(field, '21') == ('Your selected position is not valid, try again.')
    assert piskvorky.input_check(field, '5') == ('This field is not available, select another one.')




    



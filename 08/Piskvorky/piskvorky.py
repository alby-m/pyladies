import util, ai

def digit(position):
    if not position.isdigit():
        return False
    return True

def range(position):
    if position <= 19 and position >= 0:
        return True
    return False

def available(field, position):
    if field[position] != '-':
        return False
    return True

def input_check(field, position):
    if digit(position) == False:
        return('Select number')
    position = (int(position)-1)
    if range(position) == False:
        return('Your selected position is not valid, try again.')
    if available(field, position) == False:
        return('This field is not available, select another one.')
    return('ok')

def player_take(field, symbol):
    while True:
        position = input('Which position do you choose for your take? ')
        if input_check(field, position) == 'ok':
            break
        print(input_check(field, position))
    return util.take(field, int(position)-1, symbol)

def evaluate(game):
    if 'xxx' in game:
        result = ('"x" has won.')
    elif 'ooo' in game:
        result = ('"o" has won.')
    elif '-' not in game:
        result = ('It is a tie.')
    elif '-' in game:
        result = 0
    return result

def battle():
    field = '--------------------'
    print(field)
    while True:
        field = player_take(field, 'x')
        print(field)            
        if evaluate(field) != 0:
            break
        field = ai.pc_take(field, 'o')
        print(field)
        if evaluate(field) != 0:
            break
    print(evaluate(field))

#moznosti rozsirenia 2D piskvorky, pridat moznost aby si hrac volil ci je x alebo o, strategie 
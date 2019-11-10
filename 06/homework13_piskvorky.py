from random import randrange

def take(field, position, symbol):
    field_list = list(field)
    field_list[position] = symbol
    new_field = "".join(field_list)
    return new_field

def pc_take(field, symbol):
    while True:
        position = randrange(20)
        if field[position] != '-':
            continue
        break
    return take(field, position, symbol)

def player_take(field, symbol):
    while True:
        position = input('Which position do you choose for your take? ')
        if not position.isdigit():
            print('Select number.')
            continue
        position = (int(position)-1)
        if position <= 19 and position >= 0:
            if field[position] != '-':
                print('This field is not available, select another one.')
                continue  
            break
        print('Your selected position is not valid, try again.')
    return take(field, position, symbol)

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
        field = pc_take(field, 'o')
        print(field)
        if evaluate(field) != 0:
            break
    print(evaluate(field))

battle()


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

print('Result of the game is', pc_take('---ooooooooooo------','o'))

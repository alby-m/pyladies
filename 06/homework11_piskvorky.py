def take(field, position, symbol):
    field_list = list(field)
    field_list[position] = symbol
    new_field = "".join(field_list)
    return new_field

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

print('Result of the game is', player_take('--x-----------------','x'))

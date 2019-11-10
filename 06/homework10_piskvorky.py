def take(field, position, symbol):
    field_list = list(field)
    field_list[position] = symbol
    new_field = "".join(field_list)
    return new_field

print('Result of the game is', take('----------------', 1,'x'))

import util

from random import randrange

def pc_take(field, symbol):
    if field.count('-') == 0:
        raise ValueError('Field has no available spots for new take.')
    while True:
        position = randrange(len(field))
        if field[position] != '-':
            continue
        break
    return util.take(field, position, symbol)
    


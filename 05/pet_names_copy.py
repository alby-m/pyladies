def printing_modify(dict):
    dict['Harry'] = 'mouse'
    print('Change has been done below.')
    for name, animal in dict.items():
        print('{} is a {}'.format(name, animal))

def printing_add(dict):
    dict['Fred'] = 'hamster'
    print('New animal has been added below.')
    for name, animal in dict.items():
        print('{} is a {}.'.format(name, animal))

def printing_del(dict):
    del dict['Rex']
    print('Animal has been removed below.')
    for name, animal in dict.items():
        print('{} is a {}.'.format(name, animal))

pets = {'Harry':'cat', 'Rex':'dog', 'Nemo':'fish'}

printing_modify(pets)
printing_add(pets)
printing_del(pets)
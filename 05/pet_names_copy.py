def printing_modify(dict):
    modify = input('Select key of animal you want to change:')
    #check ci premenna modify ktoru zadam je v slovniku - vynimky
    dict[modify] = 'mouse'
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

# upravit / key zadane uzivatelom ako parameter funkcie / input
# doplnit vynimky 
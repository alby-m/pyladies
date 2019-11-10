positive = ('yes', 'y' )
negative = ('no','n')

def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved = input(otazka)
        odpoved = odpoved.strip()
        odpoved = odpoved.lower()
        if odpoved in positive:
            return True
        elif odpoved in negative:
            return False
        else:
            print('Nerozumím!')

if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')
class Drink:
    def __init__(self, name):
        self.name = name

    def alcohol(self, promile):
        print('{} has {} promile.'.format(self.name, promile))

class Beer(Drink):
    def occassion(self):
        print('{} is suitable for celebrations.'.format(self.name))

class Wine(Drink):
    def occassion(self):
        print('{} is suitable for solving life problems.'.format(self.name))

plzen = Beer('Plzen')
palava = Wine('Palava')

plzen.alcohol('4.5')

drinks = [Beer('Plzen'), Wine('Palava')]
for drink in drinks:
    drink.occassion()

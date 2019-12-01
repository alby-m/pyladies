from random import randrange

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def take(self, position, field):
        field_list = list(field)
        field_list[position] = self.symbol
        new_field = "".join(field_list)
        return new_field

    def digit(self, position):
        return position.isdigit()

    def range(self, position, field):
        return (position <= 19 and position >= 0)

    def available(self, position, field):
        return field[position] == '-'

    def input_check(self, position, field):
        if self.digit(position) == False:
            return('Select number')
        position = (int(position)-1)
        if self.range(position, field) == False:
            return('Your selected position is not valid, try again.')
        if self.available(position, field) == False:
            return('This field is not available, select another one.')
        return('ok')

class Pc(Player):
    def player_take(self, field):
        if field.count('-') == 0:
            raise ValueError('Field has no available spots for new take.')
        while True:
            position = randrange(len(field))
            if self.available(position, field) == False:
                continue
            break
        return(self.take(position, field))

class User(Player):
    def range(self, position, field):
        return (position <= (len(field)-1) and position >= 0)

    def input_check(self, position, field):
        result = super().input_check(position, field)
        if result == 'Select number':
            return ('Select digit')
        return result
    
    def player_take(self, field):
        while True:
            position = input('Which position do you choose for your take? ')
            if self.input_check(position, field) == 'ok':
                break
            print(self.input_check(position, field))
        return(self.take(int(position)-1, field))

class Match:
    def __init__(self, field, computer, human):
        self.field = field
        self.computer = computer
        self.human = human

    def evaluate(self):
        if 'xxx' in self.field:
            result = ('"x" has won.')
        elif 'ooo' in self.field:
            result = ('"o" has won.')
        elif '-' not in self.field:
            result = ('It is a tie.')
        elif '-' in self.field:
            result = 0
        return result

    def battle(self):
        print(self.field)
        while True:
            self.field = self.human.player_take(self.field)
            print(self.field)            
            if self.evaluate() != 0:
                break
            self.field = self.computer.player_take(self.field)
            print(self.field)            
            if self.evaluate() != 0:
                break
        print(self.evaluate())


from random import randrange
from field_2d import field

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def take(self, row, column, field):
        field[row][column] = self.symbol
        return field

    def digit(self, row, column):
        return row.isdigit() and column.isdigit()

    def range(self, row, column, field):
        return (row <= 4 and row >= 0 and column <= 4 and column >= 0)

    def available(self, row, column, field):
        return field[row][column] == '-'

    def input_check(self, row, column, field):
        if self.digit(row, column) == False:
            return('Select number of row and column')
        row = (int(row)-1)
        column = (int(column)-1)
        if self.range(row, column, field) == False:
            return('Your selected position is not valid, try again.')
        if self.available(row, column, field) == False:
            return('This field is not available, select another one.')
        return('ok')

class Pc(Player):
    def player_take(self, field):
        counting = 0
        for i in field:
            for j in i:
                if j == '-':
                    counting += 1
        if counting == 0:
            raise ValueError('Field has no available spots for new take.')
        while True:
            row = randrange(4)
            column = randrange(4)
            if self.available(row, column, field) == False:
                continue
            break
        print(self.take(row, column, field))

class User(Player):
    
    def player_take(self, field):
        while True:
            row = input('Which row position do you choose for your take? ')
            column = input('Which column position do you choose for your take? ')
            if self.input_check(row, column, field) == 'ok':
                break
            print(self.input_check(row, column, field))
        print(self.take(int(row)-1, int(column)-1, field))

# class Match:
#     def __init__(self, field, computer, human):
#         self.field = field
#         self.computer = computer
#         self.human = human

#pre overenie vyhry hraca skusit preisterovat maticu podobnym sposobom ako som pocitala prazdne policka
#na pritomnost znaku napr. x , ak najdem x, vygenerujem jeho poziciu cez dva indexz, row, column
#nasledne overujem ci na urcitych dvoch poziciach okolo sa nachadza x - vyherne pozicie
#je potreba pocitat s tym ze ak sa znak nachadza na nejakom krajom poli (napr. na pozicii v prvom riadku)
#kontrola pozicii na riadkoch nad nim nema zmysel, resp. koncila by chybou, takze je potreba bud podchytit
#podmienkou aby pri urcitych indexoch nekontrolovala nejake ine pozicie alebo aby typ chyby ignorovala
    # def evaluate(self):
    #     empty_fields = 0
    #     for i in field:
    #         for j in i:
    #             if j == '-':
    #             empty_fields += 1
    #     if 'xxx' in self.field:
    #         result = ('"x" has won.')
    #     elif 'ooo' in self.field:
    #         result = ('"o" has won.')
    #     elif empty_fields == 0:
    #         result = ('It is a tie.')
    #     elif empty_fields != 0:
    #         result = 0
    #     return result

#     def battle(self):
#         print(self.field)
#         while True:
#             self.field = self.human.player_take(self.field)
#             print(self.field)            
#             if self.evaluate() != 0:
#                 break
#             self.field = self.computer.player_take(self.field)
#             print(self.field)            
#             if self.evaluate() != 0:
#                 break
#         print(self.evaluate())

# class Board:

#     def matrix(self, rows, columns):
#     m = [['-' for i in range(columns)] for j in range(rows)]
#     return m
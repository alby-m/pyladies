import piskvorky_classes_2d
from field_2d import field

x = piskvorky_classes_2d.Pc('x')
o = piskvorky_classes_2d.User('o')

# game = piskvorky_classes.Match(field, x, o)

# game.battle()

o.player_take(field)
x.player_take(field)
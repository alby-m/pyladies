import piskvorky_classes

x = piskvorky_classes.Pc('x')
o = piskvorky_classes.User('o')

game = piskvorky_classes.Match('--------------------', x, o)

game.battle()
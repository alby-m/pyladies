class Kitten:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("{}: Meow!".format(self.name))

    def eat(self,food):
        print("{}:Meow meow! I like {}!".format(self.name, food))

mourek = Kitten('Mourek')
mourek.meow() # tu ten argument nemusim doplnovat pretoze contructom init a riadkom 11 je objektu uz priradeny
mourek.eat('mouse') # potreba dat do zatvoriek ten argument
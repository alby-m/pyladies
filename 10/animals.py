class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self,food):
        print("{}: I like {}!".format(self.name, food))


class Kitten(Animal):

    # def eat(self,food):
    #     print("{} looks at {}!".format(self.name, food))
    #     super().eat(food)

    def make_sound(self):
        print("{}: Meow!".format(self.name))

class Puppy(Animal):

    def make_sound(self):
        print("{}: Woof!".format(self.name))

class Snake(Animal):
    def __init__(self, name):
        name = name.replace('s','sss')
        name = name.replace('S','Sss')
        super().__init__(name)

animals = [Kitten('Micka'), Puppy('Azorek')]

for animal in animals:
    animal.make_sound()
    animal.eat('meat')

micka = Kitten('Micka')
azorek = Puppy('Azorek')
# standa = Snake('Stanislav')
# standa.eat('mouse')
# micka.meow()
# azorek.woof()
# micka.eat('dog food')
# azorek.eat('meat')
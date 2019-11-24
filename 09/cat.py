class Cat:
    MAX_LIVES = 9
    def __init__(self, name):
        self.lives = self.MAX_LIVES
        self.name = name

    def meow(self):
        print('{}: Meow!'.format(self.name))

    def is_alive(self):
        if self.lives > 0:
            return True
        else:
            return False

    def lose_life(self):
        if self.is_alive():
            self.lives = self.lives - 1 # alebo zapis self.lives =- 1
        else:
            print('{} is dead.'.format(self.name))

    def eat(self, food):
        if self.lives <= 0:
            print('{} is already dead, no {} will bring it back to life.'.format(self.name, food))
        else:
            if food == 'fish' and self.lives < self.MAX_LIVES:
                self.lives = self.lives + 1
            print('{} has eaten {} and now has {} lives.'.format(self.name, food, self.lives))
        
tom = Cat('Tom')

print(tom.lives)

#tom.lose_life()

print(tom.lives)

tom.eat('fish')


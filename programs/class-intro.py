class Nothing:
    pass

x = Nothing()


class Animal(object):
    pass

class Carnivores(Animal):
    food = 'meat'

    def catch(self):
        return self.food


class Lion(Carnivores):
    pass

class Tiger(Carnivores):
    color = 'yb'

    dad = 'tiger'
    mon = 'tiger'

    def __init__(self, name, color='white', food='meat'):
        self.color = color
        self.food = food


class Liger(Lion, Tiger):
    dad = 'lion'

class Tigon(Tiger, Lion):
    pass


xiaoming = Tiger('xiaoming', food='cai')
print(xiaoming.catch())

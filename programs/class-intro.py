class Nothing:
    pass

x = Nothing()

class Animal(object):
    pass

class CatFamily(Animal):
    pass

class Lion(CatFamily):
    pass

class Tiger(CatFamily):
    color = 'yb'

    dad = 'tiger'
    mon = 'tiger'

    def __init__(self, color='white'):
        self.color = color

class Liger(Lion, Tiger):
    dad = 'lion'

class Tigon(Tiger, Lion):
    pass

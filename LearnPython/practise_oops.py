

class Mobile:

    fp = 'KKK'

    def __init__(self):
        self.x = True

    @staticmethod
    def add_me(a, b):
        print(Mobile.fp)
        Mobile.fp = 'JJJ'
        return a + b

m = Mobile()
print(m.add_me(2,3))


class Father:
    def __init__(self):
        self.money = 10
        print('Father Clasee')

class Son(Father):

    def __init__(self):
        super().__init__()
        self.packet = 'ss'
        print('Son Class')

    def disp(self):
        print('Son Class')

class GrandSon(Son):
    pass

g = GrandSon()
print(g.packet)
print(g.money)

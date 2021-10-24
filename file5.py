
class atom():
    def __init__(self, meaning1, meaning2, meaning3, meaning4):
        self.meaning1 = int(meaning1)
        self.meaning2 = int(meaning2)
        self.meaning3 = int(meaning3)
        self.meaning4 = int(meaning4)

    def output(self):
        print(f' показатель 1: {self.meaning1}'
              f'\n показатель 2: {self.meaning2}'
              f'\n показатель 3: {self.meaning3}'
              f'\n показатель 4: {self.meaning4}')

    def change(self, a, b, c, d):
        self.meaning1 = int(a)
        self.meaning2 = int(b)
        self.meaning3 = int(c)
        self.meaning4 = int(d)

    def increase(self,*args,**kwargs):
        self.meaning1 = self.meaning1 + 10
        self.meaning2 = self.meaning2 + 10
        self.meaning3 = self.meaning3 + 10
        self.meaning4 = self.meaning4 + 10

    def decrease(self):
        self.meaning1 = self.meaning1 - 5
        self.meaning2 = self.meaning2 - 5
        self.meaning3 = self.meaning3 - 5
        self.meaning4 = self.meaning4 - 5

class gidro(atom):

    def __init__(self,meaning1, meaning2, meaning3, meaning4, meaning5):
        super().__init__(meaning1, meaning2, meaning3, meaning4)
        self.meaning5 = int(meaning5)

    def showgidro(self):
        print(f' показатель 1: {self.meaning1}'
              f'\n показатель 2: {self.meaning2}'
              f'\n показатель 3: {self.meaning3}'
              f'\n показатель 4: {self.meaning4}'
              f'\n показатель 5: {self.meaning5}')

# x = atom('240', '454', '120', '780')
x = gidro('240', '454', '120', '780', '234')
x.increase()
x.showgidro()

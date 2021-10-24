class x():
    def __init__(self,one):
        self.one = one
    def pr(self):
        print('one')

z = x('eee')
z.pr()

class y(x):
    def __init__(self,one,thu):
        super().__init__(one, thu)
        self.thu = thu
    def prin(self):
        print(one,thu)
fg = y('32','44')




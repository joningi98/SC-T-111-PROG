class Pair(object):
    def __init__(self, value1=0, value2=0):
        self.v1 = value1
        self.v2 = value2

    def __add__(self, other):
        return Pair(self.v1 + other.v1, self.v2 + other.v2)

    def __str__(self):
        return "Value 1: {}, Value 2: {}".format(self.v1, self.v2)


a = Pair(20, 30)
print(a)

b = Pair(40, 50)
c = a + b
print(c)

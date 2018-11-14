class DoubleList(object):
    def __init__(self, my_list=[]):
        self.my_list = my_list

    def set_AT(self, index, num):
        try:
            self.my_list[index] = num
        except IndexError:
            pass

    def __add__(self, other):
        new_double_list = []
        new_double_list.extend(self.my_list)
        new_double_list.extend(other.my_list)
        return DoubleList(new_double_list)

    def __str__(self):
        return str(self.my_list)


c1 = DoubleList([1, 4, 5, 8, 7])
c2 = DoubleList([4, 5, 7, 8])

print(c1)
print(c2)
c1.set_AT(2, 10)
print(c1)

print(c1 + c2)
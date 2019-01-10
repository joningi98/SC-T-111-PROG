import math


class Vector(list):

    def length(self):
        try:
            my_sums = sum([x**2 for x in self])
            num = math.sqrt(my_sums)
            return num
        except ValueError:
            return 0

    def __add__(self, other):
        new_list = [x + y for x, y in zip(self, other)]
        return new_list

    def scaling(self, num):
        total_value = []
        for x in self:
            total_value.append(x * num)
        self.clear()
        for y in total_value:
            self.append(y)


class VectorTest:
    """ This is a class for testing the Vector class """

    def __init__(self, list1, list2):
        self.__v1 = Vector(list1)
        self.__v2 = Vector(list2)

    def test_print(self):
        print("v1 and v2: {} {}".format(self.__v1, self.__v2))

    def test_length(self):
        print("Length of v1 and v2: {:.2f} {:.2f}".format(self.__v1.length(), self.__v2.length()))

    def test_addition(self):
        print("v1 + v2: {}".format(self.__v1 + self.__v2))

    def test_scaling(self, scalar):
        self.__v1.scaling(scalar)
        self.__v2.scaling(scalar)
        print("Scaling v1 and v2 by {}: {} {}".format(scalar, self.__v1, self.__v2))


# Main program starts here
vtest = VectorTest([2, 4], [3, -4])
vtest.test_print()
vtest.test_length()
vtest.test_addition()
vtest.test_scaling(2)

vtest = VectorTest([3, 5, -2], [2, -3, 4])
vtest.test_print()
vtest.test_length()
vtest.test_addition()
vtest.test_scaling(3)

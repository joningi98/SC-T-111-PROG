import math


class Rectangle(object):
    def __init__(self, height=0, width=0):
        self.__height = height
        self.__width = width
        self.__radius = (width / 2)
        self.circumference = 2 * math.pi * self.__radius

    def area(self):
        return float(self.__width * self.__height)

    def __eq__(self, other):
        if self.area() == other.area():
            return "The two rectangles are equally large"
        else:
            return "The two rectangles are not equal"

    def __str__(self):
        return "Length: {}, Width: {}".format(self.__height, self.__width)


r1 = Rectangle(20, 10)
r2 = Rectangle(30, 15)

print(r1)
print("%.2f" % r1.area())
print("%.2f" % r1.circumference)
print(r2)
print("%.2f" % r2.area())
print("%.2f" % r2.circumference)
print(r1 == r2)
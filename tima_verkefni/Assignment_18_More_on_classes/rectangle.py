class Rectangle(object):
    def __init__(self, length=0, width=0):
        if length < 0:
            length = 0
        if width < 0:
            width = 0
        self.__length = length
        self.__width = width

    def area(self):
        return float(self.__width) * float(self.__length)

    def perimeter(self):
        return self.__width * 2 + self.__length * 2

    def __repr__(self):
        return "Rectangle({},{})".format(self.__length, self.__width)

    def __str__(self):
        return "Length: {}, Width: {}".format(self.__length, self.__width)

    def __eq__(self, other):
        return self.area() == other.area()


a = Rectangle()
b = Rectangle(2, 3)
print(a)
print(b)
print(b.area())
print(b.perimeter())
print(b.__repr__())
print(a == b)

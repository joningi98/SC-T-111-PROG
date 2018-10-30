import math


class Circle(object):

    def __init__(self, r=0.0):
        self.__radius = float(r)

    def get_perimeter(self):
        return 2 * self.__radius * math.pi

    def get_area(self):
        return math.pi * self.__radius**2

    def set_radius(self, num=0.0):
        self.__radius = num

    def get_radius(self):
        return self.__radius

    def __str__(self):
        return "Area: {}\nPerimeter: {}".format("%.2f" % self.get_area(), "%.2f" % self.get_perimeter())


def main():
    radius = float(input("Radius of circle: "))
    circle = Circle(radius)
    print(circle)
    circle.set_radius(circle.get_radius() + 1.0)
    print(circle)


main()
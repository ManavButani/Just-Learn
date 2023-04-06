from __future__ import division
from math import pi, sqrt


class Shape:
    """Shape class contains all possible shapes"""

    def __init__(self, typee="square"):
        """Initializer with default type of square"""
        self.typee = typee  # Create an instance variable radius

    def __repr__(self):
        x="Shape({})".format(self.typee)
        """Return a formal string that can be used to re-create this instance, invoked by repr()"""
        return x

    def __eq__(self, other):
        x="Both have same shape {} ".format(self.typee)
        if self.typee == other.typee:
            return x

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()


class Circle(Shape):
    "Circle"

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        "Perimeter of Circle"
        return 2 * pi * (self.radius)

    def area(self):
        "Area of Circle"
        return pi * self.radius * self.radius


class Square(Shape):
    "Square"

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        "Perimeter of Square"
        return self.side * 4

    def area(self):
        "Area of Square"
        return self.side**2


class Rectangle(Shape):
    "Rectangle"

    def __init__(self, side1, side2) :
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        "Perimeter of Rectangle"
        return 2 * (self.side1 + self.side2)

    def area(self):
        "Area of Rectangle"
        return self.side1 * self.side2


class Triangle(Shape):
    "Triangle"

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        "Area of Triangle"
        return (self.base * self.height) / 2


class Pentagon(Shape):
    "Pentagon"

    def __init__(self, side) :
        self.side = side

    def perimeter(self):
        "Perimeter of Pentagon"
        return 5 * self.side

    def area(self):
        "Area of Pentagon"
        return 0.25 * (self.side**2) * (sqrt(5 * (5 + 2 * sqrt(5))))


class Hexagon(Shape):
    "Hexagon"

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        "Perimeter of Hexagon"
        return 6 * self.side

    def area(self):
        "Area of Hexagon"
        return (3 * sqrt(3)) / 2 * (self.side**2)


class Heptagon(Shape):
    "Heptagon"

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        "Perimeter of Heptagon"
        return 7 * self.side

    def area(self):
        "Area of Heptagon"
        return (7 / 4) * (self.side**2) * (87.77)


class Octagon(Shape):
    "Octagon"

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        "Perimeter of Octagon"
        return 8 * self.side

    def area(self):
        "Area of Octagon"
        return 2 * (1 + sqrt(2)) * (self.side**2)


if __name__ == "__main__":
    # s1=Shape("Rectangle")
    # s2=Shape("Circle")
    # s3=Shape("Rectangle")

    # print(repr(s1))
    # print(repr(s2))
    # print(s1==s3)

    c1 = Circle(10)
    s1 = Square(10)
    r1 = Rectangle(10, 5)
    t1 = Triangle(10, 2)
    p1 = Pentagon(10)
    hex1 = Hexagon(10)
    hept1 = Heptagon(10)
    oct1 = Octagon(10)

    # print(c1.area())
    print(p1 < t1)

    print(p1.area())
    print(t1.area())

    print(p1 > t1)
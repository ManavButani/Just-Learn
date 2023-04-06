from task3.shape import Shape
from math import sqrt,pi

class Circle(Shape):
    "Circle"
    def __init__(self,radius) -> None:
        self.radius = radius
    
    def perimeter(self):
        "Perimeter of Circle"
        return 2*pi*(self.radius)
    
    def area(self):
        "Area of Circle"
        return pi*self.radius*self.radius
        
class Square(Shape):
    "Square"
    def __init__(self,side) -> None:
        self.side = side
    
    def perimeter(self):
        "Perimeter of Square"
        return self.side*4
    
    def area(self):
        "Area of Square"
        return self.side**2

class Rectangle(Shape):
    "Rectangle"
    def __init__(self,side1,side2) -> None:
        self.side1 = side1
        self.side2 = side2
    
    def perimeter(self):
        "Perimeter of Rectangle"
        return 2*(self.side1+self.side2)
    
    def area(self):
        "Area of Rectangle"
        return self.side1*self.side2

class Triangle(Shape):
    "Triangle"
    def __init__(self,base,height) -> None:
        self.base=base
        self.height=height
    
    def area(self):
        "Area of Triangle"
        return (self.base*self.height)/2

class Pentagon(Shape):
    "Pentagon"
    def __init__(self,side) -> None:
        self.side = side
    
    def perimeter(self):
        "Perimeter of Pentagon"
        return 5*self.side
    
    def area(self):
        "Area of Pentagon"
        return 0.25*(self.side**2)*(sqrt(5*(5+2*sqrt(5))))

class Hexagon(Shape):
    "Hexagon"
    def __init__(self,side) -> None:
        self.side = side
    
    def perimeter(self):
        "Perimeter of Hexagon"
        return 6*self.side
    
    def area(self):
        "Area of Hexagon"
        return (3*sqrt(3))/2*(self.side**2)

class Heptagon(Shape):
    "Heptagon"
    def __init__(self,side) -> None:
        self.side = side
    
    def perimeter(self):
        "Perimeter of Heptagon"
        return 7*self.side
    
    def area(self):
        "Area of Heptagon"
        return (7/4)*(self.side**2)*(87.77)

class Octagon(Shape):
    "Octagon"
    def __init__(self,side) -> None:
        self.side = side
    
    def perimeter(self):
        "Perimeter of Octagon"
        return 8*self.side
    
    def area(self):
        "Area of Octagon"
        return 2*(1+sqrt(2))*(self.side**2)
from math import pi,sqrt

class Shape:  
    """Shape class contains all possible shapes"""
 
    def __init__(self, typee="square"):
        """Initializer with default type of square"""
        self.typee = typee  # Create an instance variable radius
 
 
    def __repr__(self):
        """Return a formal string that can be used to re-create this instance, invoked by repr()"""
        return f"Shape({self.typee})"
    
    def __eq__(self, other):
        if self.typee == other.typee:
            return f"Both have same shape {self.typee}"
    
    def __gt__(self,other):
        return self.area() > other.area()
        
    def __lt__(self,other):
        return self.area() < other.area()
 
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

if __name__ == '__main__':
    print("For Circle press 1")
    print("For Square press 2")
    print("For Rectangle press 3")
    print("For Triangle press 4")
    print("For Pentagon press 5")
    print("For Hexagon press 6")
    print("For Heptagon press 7")
    print("For Octagon press 8")
    print("To Exit press 0")

    for i in range(55):
        n=int(input("Choice : "))
        if n==0:
            exit()
        elif n==1:
            c1=Circle(int(input("Enter Radius of Circle :")))
            print(c1.area())
            print(c1.perimeter())
        elif n==2:
            s1=Square(int(input("Enter length of square :")))
            print(r1.area())
            print(r1.perimeter())
        elif n==3:
            r1=Rectangle(int(input("Enter length of Rectangle :")),int(input("Enter breadth of Rectangle :")))
            print(r1.area())
            print(r1.perimeter())
        elif n==4:
            t1=Triangle(int(input("Enter base of Triangle :")),int(input("Enter height of Triangle :")))
            print(t1.area())

        elif n==5:
            p1=Pentagon(int(input("Enter length :")))
            print(p1.area())
            print(p1.perimeter())
        elif n==6:
            hex1=Hexagon(int(input("Enter length :")))
            print(hex1.area())
            print(hex1.perimeter())
        elif n==7:
            hept1=Heptagon(int(input("Enter length :")))
            print(hept1.area())
            print(hept1.perimeter())
        elif n==8:
            oct1=Octagon(int(input("Enter length :")))
            print(oct1.area())
            print(oct1.perimeter())
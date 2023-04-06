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
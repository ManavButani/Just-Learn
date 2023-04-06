from math import pi
 
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
    
    def __gt__(self):
        pass
        
    def __lt__(self):
        pass
 
if __name__ == '__main__':
    s1=Shape("Rectangle")
    s2=Shape("Circle")
    s3=Shape("Rectangle")
    
    print(repr(s1))
    print(repr(s2))
    print(s1==s3)
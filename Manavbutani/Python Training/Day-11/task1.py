from __future__ import division
from __future__ import print_function
from math import pi,sqrt


class Circle():
    "Circle"
    def __init__(self,area) -> None:
        self.area = area
    
    def get_length(self):
        return sqrt(self.area/pi)

class Square():
    "Square"
    def __init__(self,area) -> None:
        self.area = area
    
    def get_length(self):
        return sqrt(self.area)

if __name__ == '__main__':
    c1=Circle(314.15)
    s1=Square(100)
    print("radius: ",c1.get_length())
    print("length: ",s1.get_length())
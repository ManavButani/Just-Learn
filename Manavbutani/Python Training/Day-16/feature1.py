"""Feature 1 is related to design of avatar
"""

class Avatar:
    """It is parent class of all features to beautiful design of your avatar
    """
    def __init__(self) -> None:
        """Refer an pointer to object """
        pass
        
class BodyShape(Avatar):
    """_summary_

    Args:
        Avatar (_type_): Initialize Body and Shape of Head
    """
    def __init__(self):
        super().__init__()
        
    def SquareHead(self):
        pass
    
    def RoundHead(self):
        pass
        
    def LongHeight(self):
        pass
    
    def ShortHeight(self):
        pass


class ColorAvatar(Avatar):
    """_summary_

    Args:
        Avatar (_type_): _Gives color to the Avatar_
    """
    
    def __init__(self) -> None:
        super().__init__()
    
    def Color(self,color):
        self.color = color
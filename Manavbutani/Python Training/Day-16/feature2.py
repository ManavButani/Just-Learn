"""Feature 2 is about create Room to join and wait for players until strength limit reach to 15"""
from feature1 import Avatar 

class Room(Avatar):
    
    cnt=0
    def __init__(self) -> None:
        super().__init__()
        self.cnt+=1
        
    def join(self):
        print("Joined")
    
    def leave(self):
        self.cnt-=1

class Join(Room):
    """_summary_

    Args:
        Room (_type_): _Join the Game_
    """
    
    def __init__(self) -> None:
        super().__init__()
        
    def join():
        pass
    
class Leave(Room):
    """_summary_

    Args:
        Room (_type_): _Leave the Room_
    """
    def Leave(self):
        self.cnt-=1
        

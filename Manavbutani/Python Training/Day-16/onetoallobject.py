from feature1 import BodyShape,ColorAvatar
from feature2 import Room
from feature3 import Movement
from chatroom import Chat

class MyRun(BodyShape,ColorAvatar,Room,Movement,Chat):
    def __init__(self):
        print(f"All in one is running")
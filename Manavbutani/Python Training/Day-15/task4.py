"""
4. Create a decorator which makes a class singleton.
 In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance.
This is useful when exactly one object is needed to coordinate actions across the system.
 Reference: https://en.wikipedia.org/wiki/Singleton_pattern

 When used on class It should show similar output as “TheOne” class as follows:

 >>> first_one = TheOne()
 >>> another_one = TheOne()

 >>> id(first_one)
 140094218762280
 >>> id(another_one)
 140094218762280

 >>> first_one is another_one
 True
"""
def singleton(class_):
    instance=[None]
    def inner():
        if instance[0] is None:
            instance[0]=class_()
        return instance[0]
    return inner

@singleton
class TheOne:
    def __init__(self) -> None:
        print("Created...")
    
if __name__ == "__main__":
    x=TheOne()
    y=TheOne()
    
    print(f"First_one id: {id(x)}")
    print(f"Another_one id: {id(y)}")
    
    if x is y:
        print(True)
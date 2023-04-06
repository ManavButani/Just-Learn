"""
Write a method which takes 2 integers as arguments and A) returns the sum of them if both are positive or
B) raises a ValueError exception if either of them are negative. Write unit tests to test the method with
100% coverage.

"""
def sum(x,y):
    if int(x)<0 or int(y)<0:
        raise ValueError("Only positive numbers are allowed")
    else:
        return int(x)+int(y)



    
if __name__=="__main__":
    sum(input("Enter number1 "),input("Enter number2 "))
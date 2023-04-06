def swap1(a,b):
    a,b = b,a
    print("Swapping using comma operator",a,b)
    
def swap2(a,b):
    temp=a
    a=b
    b=temp
    print("Swapping using extra variable",a,b)

    
if __name__=="__main__":
    a,b = map(int,input("Enter Two Numbers \n ").rsplit())
    print("Before swapping numbers are ",a,b)
    
    swap1(a,b)
    swap2(a,b)
    
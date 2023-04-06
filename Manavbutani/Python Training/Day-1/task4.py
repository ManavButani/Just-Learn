def manav(a,b,c):
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        print(a/b)
    else:
        print(f"Please enter valid operation")
        

if __name__=="__main__":
    a,b = map(int,input("Enter Two Numbers \n ").rsplit())
    # print(a,b)
    c = input("Operation to perform \n")
    
    manav(a,b,c)
    
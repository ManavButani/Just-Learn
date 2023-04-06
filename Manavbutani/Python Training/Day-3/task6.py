import argparse

class Task6():
    """This is task6
    """
    
    def __init__(self,n1,n2,n3) -> None:
        self.n1=n1
        self.n2=n2
        self.n3=n3
        self.operation()
    
    def operation(self):
        if self.n3 == "add":
            print(self.n1+self.n2)
        else:
            if args.opera == "sub":
                print(self.n1-self.n2)
            else:
                print(self.n1*self.n2)
    
    def __del__(self):
        print("Destructing Standard Inputs")
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1",help="first number")
    parser.add_argument("--number2",help="second number")
    parser.add_argument("--opera",help="operation wants to perform on numbers",choices=["add","sub","mul"])
    
    args = parser.parse_args()
    n1=int(args.number1)
    n2=int(args.number2)
    
    r=Task6(n1,n2,args.opera)
    del r
    
    
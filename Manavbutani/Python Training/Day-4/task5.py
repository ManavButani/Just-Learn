
class MyFiles():
    def __init__(self,name,choice):
        self.name=name
        self.choice=choice
        self.mychoice()
    
    
    def mychoice(self):
        try:
            f = open(self.name, self.choice)
        except ValueError as e:
            print("Please enter valid mode of file")
        
        if self.choice == "a":
            print("enter the content you want to append into files ")
            f.write("\n")
            f.write(input())
        
        try:
            if self.choice == "r":
                print(f.readlines(-1))
        except TypeError as e:
            print(e)
            
        
            
        
if __name__ == "__main__":
    
    try:
        f1=MyFiles(input("Enter File Name "),input("Enter Your Choice "))
    except FileExistsError as e:
        print("File Already Exist")
t=int(input("Total number of students "))
data=[]
for i in range(t):
    fname=input("Enter First Name: ")
    lname=input("Enter Last Name: ")
    roll_no=int(input("Enter roll no: "))
    data.append([fname,lname,roll_no])

for i in range(len(data)):
    print(data[i])
    
print(f"If you want to sort using First Name then enter 0: ") 
print(f"If you want to sort using Last Name then enter 1: ") 
print(f"If you want to sort using First Name then enter 2: ")
n=int(input("Enter your choice"))

if n==0:
    data.sort()
elif n==1:
    data.sort(key=lambda x: x[1])
elif n==2:
    data.sort(key=lambda x: x[2])
else:
    print(f"Invalid Choice")
    exit()

print("After Sorting: ")



for i in range(len(data)):
    print(data[i])

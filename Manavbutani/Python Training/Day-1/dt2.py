n=int(input("Enter size of list "))
l=[]
for i in range(n):
    print("Enter element",i+1)
    l.append(int(input()))
    
print(f"{l}")
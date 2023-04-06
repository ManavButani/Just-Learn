t=input("Enter total number of Students: ")
dict = {}

for i in range(int(t)):
    n = input("Enter Student name  ")
    dict.update({n: list(map(int,input().rsplit()))})

for i,j in dict.items():
    print(i,"total marks is",sum(j))
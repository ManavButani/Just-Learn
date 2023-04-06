import math

t=input("Enter total number of Students: ")
dict = {}
list1 = []

for i in range(int(t)):
    n = input("Enter Student name  ")
    dict.update({n: list(map(int,input().rsplit()))})

for i,j in dict.items():
    print(i,"total percentage is",(sum(j)/(len(j)*100))*100)
    list1.append([i,j])
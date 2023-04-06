x,y = map(int,input("Enter positions : ").rstrip().split())
s=input("Enter a String : ")
l=[]
new=""
for i in s:
    l.append(i)
   
l[x] = l[y]

for i in l:
    new+=i
print("Final Output is ",new)
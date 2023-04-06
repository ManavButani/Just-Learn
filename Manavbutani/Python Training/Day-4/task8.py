import re

if __name__=="__main__":
    s=input("Enter a Date in yyyy-mm-dd format: ")
    x=re.findall("\d{4}-\d{2}-\d{2}",s)
    x=x[0]
    # print(x)
    if len(x)!=10:
        print("Invalid Input")
        
    m=re.findall("-\d{2}-",s)
    y=re.findall("\d{4}-",s)
    d=re.findall("-\d{2}$",s)
    
    x=d[0]+m[0]+y[0]
    x=re.findall("\d{2}-\d{2}-\d{4}",x)
    print("dd-mm-yyyy = ",x[0])

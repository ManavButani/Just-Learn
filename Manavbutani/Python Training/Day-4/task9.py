import re

if __name__ == "__main__":
    k=0
    
    s=input("Enter Valid IPV4 address")
    d=input("Enter Valid IPV6 address")
    
    s=re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",s)
    
    s=re.findall("\d{1,3}",s[0])
    if len(s)<4:
        print("Invalid IPV4")
        k=1
        
    if k!=1:
        for i in s:
            if int(i)>255:
                print("Invalid IPV4")
        else:
            print("Valid IPV4")
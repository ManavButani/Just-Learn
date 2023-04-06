if __name__=="__main__":
    s=input("Enter a String : ")
    if len(s)<3:
        print(f"Length should be at least three")
        exit()
    k=len(s)
    z=s[k-3]+s[k-2]+s[k-1]
    
    if k<3:
        print(s)
    else:
        if z=="ing":
            print(s+"ly")
        else:
            print(s+"ing")
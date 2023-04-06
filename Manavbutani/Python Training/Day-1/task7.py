if __name__=="__main__":
    s = input("Enter a string ------")
    
    k=len(s)
    if k<2:
        print("")
    else:
        print(s[0]+s[1]+s[k-2]+s[k-1])
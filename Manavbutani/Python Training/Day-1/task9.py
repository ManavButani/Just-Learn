def remove_odd(s):
    z=""
    for i in range(len(s)):
        if i%2!=0:
            z+=s[i]
    print(z)            

if __name__=="__main__":
    s=input("Enter a String : ")
    remove_odd(s)
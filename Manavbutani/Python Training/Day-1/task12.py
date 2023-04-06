import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("s",help="Enter String")
    
    args = parser.parse_args()
    s=args.s
    print("******",s)
    
    z=""
    l=[]
    for i in range(len(s)):
        if s[i] not in [" ", ".", ",", "\n"]:
            z+=s[i]
            # print("-",z)
        else:
            if z!="":
                l.append(z)
                # print("--",z)
                z=""
    
    
    for i in range(len(l)):
        cnt=1
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                cnt+=1
                l[j]="*"
        
        if l[i]!="*":
            print(l[i],cnt)
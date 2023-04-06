def insert_in_middle(s):
    k=len(s)
    z=""
    if k%2==0:
        # first half of a string
        for i in range(0,k//2,1):
            z=z+s[i]
        # print("-",z)
        #middle half
        z=z+s[:]
        # print("--",z)
        
        #second half of a string
        for j in range(k//2,k,1):
            z=z+s[j]

        
    else:
        for i in range(0,k//2,1):
            z=z+s[i]
        # print("-",z)
        #middle half
        z=z+s[:]
        # print("--",z)
        
        #second half of a string
        for j in range((k//2)+1,k,1):
            z=z+s[j]
        
            
    print(z)
if __name__ == "__main__":
    s = input("Enter a String : ")
    insert_in_middle(s)
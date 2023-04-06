if __name__ == "__main__":
    s = input("Enter anything : ")
    l=[]
    c = input("Enter character to count frequency : ")
    cnt=0
    for i in s:
        if i==c:
            cnt+=1
    
    print(f"{c} repeats {cnt} times")
    # for j in range(0,len(s),1):
    #     z=1
    #     if s[j] not in r:
    #         for i in range(j+1,len(s),1):
    #             if s[j]==s[i]:
    #                 z+=1
            
    #         r.append(s[j])
    #         print(s[j],"repeats ",z," times")
            
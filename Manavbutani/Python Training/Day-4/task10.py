import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

if __name__=="__main__":
    y=[]
    y1=[]
    s=input("Enter a XML content without a space: ")
#     # \<\w{3}\>\d{3}\<(\/)\w{3}\>
    x=re.findall(">\d{3}<\/",s)
    # print(x)
    
    x1=re.findall("<\w{3}",s)
    # print(x1)
    for m in x:
        y.append(re.findall("\d{3}",m))
    # print(y)
    for m in x1:
        y1.append(re.findall("\w{3}",m))
    # print(y1)
    
    thisdict={}
    
    for i in range(len(x1)):
        thisdict[y1[i][0]]=y[i][0]
    
    print(thisdict)
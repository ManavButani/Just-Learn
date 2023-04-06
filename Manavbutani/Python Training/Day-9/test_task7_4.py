import re
import pytest

def main(s):
    k=0
    
    # s=input("Enter Valid IPV4 address")
    
    s=re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",s)
    
    s=re.findall("\d{1,3}",s[0])
    if len(s)<4:
        print("Invalid IPV4")
        k=1
        
    if k!=1:
        for i in s:
            if int(i)>255:
                print("Invalid IPV4")
                return 0
        else:
            print("Valid IPV4")
            return 1
        
@pytest.mark.parametrize("input,output",[("266.0.287.2",0),("255.0.255.2",1)])
def test_task7_4(input,output):
    assert main(input)==output
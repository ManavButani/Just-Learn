import json

class find_value:
    def __init__(self,is_found) -> None:
        self.is_found=is_found

    def find_key(self,root, key_to_check):
        if isinstance(root, dict):
            for key, value in root.items():
                if key_to_check == key:
                    self.is_found = True
                    print("The value of ",key," is ",value)
                elif isinstance(value, (list,dict)):
                    self.find_key(value, key_to_check)
        elif isinstance(root, list):
            for i in root:
                if isinstance(i, (dict,list)):
                    self.find_key(i, key_to_check)



f = open(
    "demo.json"
)
j = json.load(f)
obj1=find_value(False)
key_to_search=input("Enter the value of the that u want to find:")
obj1.find_key(j,key_to_check=key_to_search)
if not obj1.is_found:
    print("The key is not present")

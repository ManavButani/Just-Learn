import xml.etree.ElementTree as ET

class RE():
    def __init__(self,root,level) -> None:
        self.root=root
        self.level=level
        self.recursive(self.root,self.level)

    def recursive(self,root,level):
        for child in root:
            print(level*"\t",child.attrib["name"])
            self.recursive(child,level+1)
    
if __name__=="__main__":
    mytree = ET.parse('Sample.xml')
    root = mytree.getroot()
    
    obj=RE(root,0)
    
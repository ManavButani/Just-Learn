import sys
from xml.dom import minidom
def main():
    data = minidom.parse("sam.xml")
    xml_string = data.toprettyxml()
    sys.stdout.write(xml_string)
    sys.stdout.flush()
if __name__ == "__main__":
    main()
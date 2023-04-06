"""
Define 3 objects: bytes, str, unicode. Check whether
they are the type of base string or not for Py2 and Py3
"""

"""
Conclusion:

Py2 type: str str str
Py3 type: bytes str str
"""

def main():
    # Object of type "bytes"
    bytes_object = bytes(b"test-bytes")
    
    # Object of type "str"
    str_object = str("test-str")
    
    # Object of type "unicode"
    unicode_object = "test-unicode"
    
    print("'bytes' object")
    print("Value --> {}".format(bytes_object))
    print("Type --> {}".format(type(bytes_object)))

    print("'str' object")
    print("Value --> {}".format(str_object))
    print("Type --> {}".format(type(str_object)))

    print("'unicode' object")
    print("Value --> {}".format(unicode_object))
    print("Type --> {}".format(type(unicode_object)))

if __name__ == "__main__":
    main()

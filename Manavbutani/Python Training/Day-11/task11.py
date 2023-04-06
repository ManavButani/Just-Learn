"""
For the dictionary: owners = {"John": u"Dog", "Jane": b"Cat", "Jerome": u"Parrot", "Jenny": b"Dog", "Jared": u"Cow", "James": b"Dog", "Jeremy": b"Cow", "Jon": b"Parrot"},
write a program to swap the keys and values and store in a new dictionary 'pets'. Is the resultant dictionary 'pets' same for both Py2 and Py3? 
What are the changes required so that they give the same output on both Python versions.
"""
import sys
owners={
    "John": u"Dog",
    "Jane": b"Cat",
    "Jerome": u"Parrot",
    "Jenny": b"Dog",
    "Jared": u"Cow",
    "James": b"Dog",
    "Jeremy": b"Cow",
    "Jon": b"Parrot"
}
pets={}
for key,value in owners.items():
    if isinstance(value, bytes):
        if sys.version_info.major == 3:
            pets[value.decode("utf-8")] = key
        else:
            pets[str(value)] = key
    else:
        pets[value] = key
print(pets)
"""
Before adding the type checking block
Output in python2:
{'Jeremy': 'Cow', 'Jenny': 'Dog', 'James': 'Dog', 'Jane': 'Cat', 'Jared': u'Cow', 'John': u'Dog', 'Jerome': u'Parrot', 'Jon': 'Parrot'}
{u'Parrot': 'Jon', 'Dog': 'John', 'Cow': 'Jared', 'Cat': 'Jane'}
"""
"""
Output in python3:
{'John': 'Dog', 'Jane': b'Cat', 'Jerome': 'Parrot', 'Jenny': b'Dog', 'Jared': 'Cow', 'James': b'Dog', 'Jeremy': b'Cow', 'Jon': b'Parrot'}
{'Dog': 'John', b'Cat': 'Jane', 'Parrot': 'Jerome', b'Dog': 'James', 'Cow': 'Jared', b'Cow': 'Jeremy', b'Parrot': 'Jon'}
"""
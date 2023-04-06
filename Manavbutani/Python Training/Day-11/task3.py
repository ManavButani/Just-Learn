"""
For Python2, we have an inbuilt “basestring” class. 
Implement the same for Python3. When the basestring is accessed for Py2and Py3,
do we have the same result?

"""

unicode_obj = u"This is Unicode"
a = "This is simple string"
print(type(unicode_obj))
print(type(a))
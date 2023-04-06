import task3

s1 = task3.Shape("Magnate")
print(repr(s1))

s2 = task3.Circle(10)
s3 = task3.Circle(10.1)

print(s2>s3)
print(task3.version.__version__)
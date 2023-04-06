from task5_parent import Employee

print("Using Pickle")

e1 = Employee(input("Enter Name"),int(input("Enter Name")),input("Enter gender"))
e2 = Employee(input("Enter Name"),int(input("Enter Name")),input("Enter gender"))

e1.serialization_pickle()
print(e1.deserialization_pickle())

e2.serialization_json()
print(e2.deserialization_json())
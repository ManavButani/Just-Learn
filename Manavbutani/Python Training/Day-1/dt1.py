x=float(input("Enter balance of account : "))
y=float(input("Enter withdrawal amount "))

if y%2!=0:
    z=x-y-10.50
    if z<0:
        print("Insufficient Balance ")
    else:
        print("Successful withdrawal")
        print("Amount remains",z)
else:
    print(f"Please enter odd withdrawal amount")
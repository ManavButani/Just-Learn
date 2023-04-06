if __name__ == "__main__":
    try:
        j=int(input("Enter Integer Number "))
        k=int(input("Enter Integer Number "))
        print("Division is : j/k = ",j/k)
    except (ZeroDivisionError) as e:
        print("Divide by Zero exception...!!!")
    except ValueError as e:
        print("Invalid inputs, expected integers...!!! ")
    finally:
        print("I am from finally")
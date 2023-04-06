if __name__ == "__main__":
    k=0
    try:
        j=float(input("Enter Positive Number "))
        if j<0:
            raise ValueError("Please Enter positive number")
    except ValueError as e:
        print("Value error: --",e)
    else:
        k=1
    finally:
        if k==1:
            print("Successful")
        else:
            print("Unsuccessful")
        
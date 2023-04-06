if __name__ == "__main__":
    k=0
    try:
        j=int(input("Enter Integer "))
        i=float(input("Enter Float "))
    except ValueError as e:
        print("Value error: --",e)
        print("Please Enter Valid Input")
    else:
        k=1
    finally:
        if k==1:
            print("Successful")
        else:
            print("Unsuccessful")
        
class MyError(Exception):
    pass

if __name__ == "__main__":
    k=0
    try:
        j=int(input("Enter Integer "))
    except ValueError as e:
        try:
            raise MyError("Entered value can't be converted to integer!!")
        except MyError as e:
            print(e)
    
    
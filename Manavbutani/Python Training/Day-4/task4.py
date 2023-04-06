class OverAgeError(Exception):
    pass

class UnderAgeError(Exception):
    pass

# try:
#     raise MyCustomError("This is CustomError..!!")
# except MyCustomError as e:
#     print(e)

if __name__ == "__main__":
    try:
        j=float(input("Enter Your Age: "))
        if j<18:
            raise UnderAgeError
        elif j>40:
            raise OverAgeError
    except UnderAgeError:
        print(f"You are UnderAge by {18-j} years..!!")
    except OverAgeError:
        print(f"You are OverAge by {j-40} years..!!")
    except Exception:
        print(e)
        
def multiply(n):
    def manav(x):
        return n*x
    return manav

if __name__ == "__main__":
    make_double = multiply(int(input("Enter number 1st number")))
    print(make_double(int(input("Enter number 2nd number")))) # should print "10"
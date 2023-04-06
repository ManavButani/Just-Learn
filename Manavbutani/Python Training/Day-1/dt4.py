def generator(N):
    value = 1
    while value<=N:
        yield value
        value+=1
        
if __name__ == "__main__":
    N=int(input("Enter number"))
    for k in generator(N):
        print(f"{k}")
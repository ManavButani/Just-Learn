import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n1",help="Enter number 1")
    parser.add_argument("n2",help="Enter number 2")
    parser.add_argument("n3",help="Enter number 3")
    
    args=parser.parse_args()
    a=int(args.n1)
    b=int(args.n2)
    c=int(args.n3)
    
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    print(max(l), "is largest")
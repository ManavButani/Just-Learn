import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1",help="Input Number which will check number category")
    args=parser.parse_args()
    n=int(args.number1)
    
    if n>0 and n<10:
        print("Small")
    else:
        if n>10 and n<100:
            print("Medium")
        else:
            if n<1000:
                print("Large")
            else:
                if n>1000:
                    print("Invalid")
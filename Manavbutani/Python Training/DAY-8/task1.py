import logging

def display_words(x):
    try:
        logging.basicConfig(filename="newfile.log",
                            style="{",
                    format='{asctime}- {message}',
                    filemode='w')
        f = open(x, "r")
    except FileNotFoundError as e:
        logging.warning("File does not exist")
    except Exception as e:
        print("Handled")
    else:
        j=""
        while True:
            c=f.read(1)
            if c in [" ","\n","\t"]:
                if len(j)<4:
                    logging.critical(f"Critical: word is not enough lengthy {j}")
                j=""
            else:
                j+=c
            
            if c=="":
                break

if __name__=="__main__":
    display_words(input("Enter File name: "))
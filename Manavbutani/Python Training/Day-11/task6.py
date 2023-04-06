"""
Define 3 objects: bytes, str, unicode. Print these 3 objects,
write them into a file, write them in the console.
"""
import sys
def main():
    unicode_obj = u"unicode sample data"
    string_obj = "string sample data"
    byte_obj = b"byte sample data"
    try:
        file_write = open("filedata.txt", "w")
    except FileNotFoundError as error:
        sys.stdout.write(error)
    else:
        file_write.write("{}\n{}\n{}".format(unicode_obj, string_obj, byte_obj))
        file_write.close()
    try:
        file_read = open("filedata.txt", "r+")
    except FileNotFoundError as error:
        sys.stdout.write(error)
    else:
        sys.stdout.write(file_read.read())
        file_read.close()
        sys.stdout.flush()
if __name__ == "__main__":
    main()
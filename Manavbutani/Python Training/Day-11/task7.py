"""
Create a gzip of a single simple text file, write some text in it.
Open the gzip file programmatically and read the contents. The file should be read
in Py2 and Py3. Raise FileNotFoundError if the gzip file doesn't exist.
After reading the file, write the same content in a new gzip file.
"""
from __future__ import print_function
import gzip
import shutil
def main():
    try:
        file_write = gzip.GzipFile("manav.txt.gz", "wb+")
        data = b"This is sample text file."
        file_write.write(data)
        file_write.close()
        
        with gzip.open("manav.txt.gz", "rb") as file_in:
            with open("manav1.txt", "wb+") as file_out:
                shutil.copyfileobj(file_in, file_out)

    except FileNotFoundError as error:
        print("FileNotFoundError : {}".format(error))

if __name__ == "__main__":
    main()
"""
Using urllib.parse, make a URL browser friendly, i.e., a blank space should be converted to %20,
: should be replaced with %3A. Read the input from command line as an argument.
Apply validations and then parse the URL. User can pass multiple URLs too.
Make your code compatible to accept n number of URLs.
"""
from six.moves import input as raw_input

try:
    from urllib.parse import urlparse, quote

except ImportError:
    from urlparse import urlparse
    from urllib import quote

def check_url(input_url):
    parse_url = urlparse(input_url)
    check = all(
        [
            parse_url.scheme,
            parse_url.netloc,
        ]
    )
    if check:
        output = quote(input_url)
        print(output)
    else:
        print("Invalid URL")

def main():
    url_input = str(raw_input("Enter Url: "))
    check_url(url_input)

if __name__ == "__main__":
    main()
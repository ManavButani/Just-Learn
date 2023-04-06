""" Write a python program to find Urls from a given string.(Regex)
"""
import re
user_input = input("Enter String: ")
urls = re.findall(
    r"http[s]?://(?:[a-zA-Z]|[\d]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
    user_input,
)
print(urls)
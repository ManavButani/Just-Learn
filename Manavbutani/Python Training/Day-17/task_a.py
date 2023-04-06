""" a.Write Synchronous version with requests lib"""

import time
import requests

session=requests.session()

def time_taken(func):
    """decorator function for calculating the time
    Args:
        func (function): function to be wrapped by decorator
    """
    def inner(*args,**kwrgs):
        start=time.time()
        func(*args,**kwrgs)
        end=time.time()
        print(f"time taken:{end-start}")
    return inner

@time_taken
def synchronous():
    """using synchronous
    """
    api_endpoint="https://source.unsplash.com/random"
    for i in range(5):
        response=session.get(api_endpoint,timeout=10)
        if response.status_code==200:
            with open(f"image_{i}.jpg",'wb') as file:
                file.write(response.content)
        else:
            print("no response received")

if __name__ == "__main__":
    print("==============using synchronous============")
    synchronous()
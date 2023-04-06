"""d.Write multiprocessing version same"""

import time
import requests
from multiprocessing import Process

session=requests.session()

def hit_api(session,i):
    """hits the api endpoint
    Args:
        number (file number ): to create separate file for each
    """
    api_endpoint="https://source.unsplash.com/random"
    response=session.get(api_endpoint,timeout=10)
    if response.status_code==200:
        with open(f"image_{i}.jpg",'wb') as file:
            file.write(response.content)
    else:
        print("no response received")

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
def api_multiprocessing():
    """using threadpool
    """
    processes=[]
    for i in range(5):
        process=Process(target=hit_api,args=(session,f"{i}",))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


if __name__ == "__main__":
    print("==============using multiprocessing============")
    api_multiprocessing()
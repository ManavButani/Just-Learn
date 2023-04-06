"""b.Write multithreading version (with Threading and Threadpoolexecutor both)"""

import time
import requests
import threading
from concurrent.futures import ThreadPoolExecutor

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
def api_multithreading():
    """using multithread
    """
    threads=[]
    session=requests.session()
    for i in range(5):
        thread=threading.Thread(target=hit_api,args=(session,i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

@time_taken
def api_threadpool():
    """using threadpool
    """
    images=[0,1,2,3,4]
    session=requests.session()
    with ThreadPoolExecutor(max_workers=len(images)) as executor:
        for i in range(len(images)):
            executor.submit(hit_api,session,i)

if __name__ == "__main__":
    print("==============using multithreading============")
    api_multithreading()
    print("==============using ThreadpoolExecutor============")
    api_threadpool()
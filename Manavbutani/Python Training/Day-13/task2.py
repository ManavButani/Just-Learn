"""
Implement basic function for finding factorial of single number. (function must sleep or 0.001second after each iteration)
a. Take list of N numbers and find their factorial without using multithreading and show after results of all numbers are ready.
b. Take list of N numbers and find their factorial using multithreading and show after result of all number is ready.
c. Analyse time taken, cpu usage, memory usage.

"""
from multiprocessing.pool import ThreadPool
# import threading
import time
import math

l=[]
def without(n):
    time.sleep(0.001)
    return math.factorial(n)

def with_threads(n):
    time.sleep(0.001)
    return math.factorial(n)

if __name__ == "__main__":
    t1=time.time()
    arr=[x for x in range(1,50)]
    result=[]
    for i in arr:
        result.append(without(i))
    print(result)
    print(f"Time taken in process without multithreading is {time.time()-t1}")
    
    t1=time.time()
    n_threads = ThreadPool(processes=5)
    result = n_threads.map(with_threads,[x for x in range(1,50)])
    n_threads.close()
    n_threads.join()
    for i in result:
        print(str(i),end=",")
    print(f"\nTime taken in process with multithreading is {time.time()-t1}")
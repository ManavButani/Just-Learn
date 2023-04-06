"""

3. Implement basic function for finding n'th fibonacci number of series. (function must sleep for 0.001second after each iteration)
a. Take list of N numbers and find respective fibonacci number without using multiprocessing and show after results of all
numbers are ready.
b. Take list of N numbers and find their respective fibonacci number using multiprocessing and show after results of all numbers
are ready.
c. Analyses time taken, cpu usage, memory usage

"""

from multiprocessing import Pool
import time

def without(n):
    time.sleep(0.001)
    l=[0,1]
    if n in [0,1]:
        return n
    else:
        for i in range(n-1):
            x=l[len(l)-2]+l[len(l)-1]
            l.append(x)
        return l.pop()
    
def with_mp(n):
    time.sleep(0.001)
    l=[0,1]
    if n in [0,1]:
        return n
    else:
        for i in range(n-1):
            x=l[len(l)-2]+l[len(l)-1]
            l.append(x)
        return l.pop()
    
if __name__ == "__main__":
    t1=time.time()
    arr=[x for x in range(0,50)]
    result = []
    for i in arr:
        result.append(without(i))
    
    print(f"Time taken without multiprocessing is {time.time()-t1}")
    print(f"{result}")
    
    t1=time.time()
    p = Pool(processes=5)
    result = p.map(with_mp,arr)
    p.close()
    p.join()
    print(f"Time taken with multiprocessing is {time.time()-t1}")
    print("\n")
    for i in result:
        print(f"{i}",end=",")
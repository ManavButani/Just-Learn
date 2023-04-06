"""Implement simple function which takes name as input and returns "hello <name>" after 1 second.
a. Do it for N names using multithreading and multiprocessing."""

import multiprocessing,threading,time

def greet_process(n):
    time.sleep(1)
    return f"Hello {n}"

def greet_thread(n):
    time.sleep(1)
    return f"Hello {n}"

if __name__ == "__main__":
    arr1 = ['manav','krenil','rajan','ram']
    arr2 = ['malkesh','shyam','kano','laxman']
    
    t1=time.time()
    
    th1=threading.Thread(target=greet_thread, args=(arr1,))
    th2=threading.Thread(target=greet_thread, args=(arr2,))
    
    th1.start()
    th2.start()
    
    th1.join()
    th2.join()
    print(f"Threading Done in {time.time()-t1}")
    
    t1=time.time()
    
    pr1=multiprocessing.Process(target=greet_process, args=(arr1,))
    pr2=multiprocessing.Process(target=greet_process, args=(arr2,))
    
    pr1.start()
    pr2.start()
    
    pr1.join()
    pr2.join()
    print(f"Processing Done in {time.time()-t1}")
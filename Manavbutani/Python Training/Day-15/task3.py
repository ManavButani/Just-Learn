"""
3. Calculate time taken by function in the function execution using decorator.
 For example:
 >>> waste_some_time(1)
 Finished 'waste_some_time' in 0.0010 secs
 >>> waste_some_time(999)
 Finished 'waste_some_time' in 0.3260 secs

"""
import time

def decorator(func):
    def child(n):
        x=time.time()
        func(n)
        print(n)
        z=time.time()-x
        print(f"Finished '{func.__name__}' in {z} seconds")
    return child


@decorator
def waste_some_time(num):
    time.sleep(0.5)
    for _ in range(num):
        pass

print(f"{waste_some_time(999)}")
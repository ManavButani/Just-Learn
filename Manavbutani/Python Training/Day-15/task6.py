import time

cache = {0:0,1:1}
def deco(func_fibbo):
    
    global cache
    def wrapper(num):
        if num not in list(cache.keys()):
            cache[num] = func_fibbo(num)
        else:
            return cache[num]
    print(cache)
    return wrapper

@deco
def fibo(n):
    if n in [0,1]:
        return n
    else:
        try:
            return fibo(n-1)+fibo(n-2)
        except Exception:
            pass
    
if __name__ == "__main__":
    t1=time.time()
    fibo(10)
    print(fibo(10))
    print(f"First time execution takes is {time.time()-t1}")
    
    t1=time.time()
    fibo(10)
    print(f"Second time execution takes is {time.time()-t1}")
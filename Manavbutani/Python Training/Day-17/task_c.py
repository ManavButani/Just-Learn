"""c.Write a async version for same"""

import requests
import asyncio
import time

async def asyncio_hit_api(i):
    api_endpoint="https://source.unsplash.com/random"
    session=requests.session()
    response=session.get(api_endpoint,timeout=10)
    if response.status_code==200:
        with open(f"image_{i}.jpg",'wb') as file:
            file.write(response.content)
    else:
        print("no response received")

async def api_asyncio():
    """using async io"""
    for i in range(5):
        await asyncio.gather(asyncio_hit_api(f"_async_{i}"))
        
if __name__ == "__main__":
    print("==============using async io============")
    start=time.time()
    asyncio.run(api_asyncio())
    end=time.time()
    print(f"time taken:{end-start}")

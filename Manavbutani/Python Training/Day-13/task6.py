"""
Add following features in above example.
a. Take max no. of threads N for api call and M for writing into file from user.
b. Make list of latitude and longitude and instead of passing it to function all thread must read lat. & long,
from the same global list.
c. Make initially blank output list and all threads must write output to that list only.
d. Threads which are writing output to file must take input from list created in C.
(Hint: Use threadpool, Use queue for inter-thread communication)

"""
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from mapquest import MapQuest
import json
import logging
from queue import Queue

lock = Lock()

list_of_lat_long = [
        [21.1702, 72.8311],
        [23.0225, 72.5714],
        [22.3072, 73.1812],
        [21.2049, 72.8411],
        [22.6916, 72.8634],
    ]

def filehandling(information):
    filename = "manav.txt"
    global lock
    with lock:
        with open(filename, "a+") as f:
            print(type(information))
            print(information)
            # json.dump(information,f,indent=4) 
            # json.dumps(information,f,indent=4)
            f.write(json.dumps(information))
            f.write("\n")

def information_from_mapquest_api(client):
    global list_of_lat_long
    output=[]
    q=Queue()
    
    with ThreadPoolExecutor(max_workers=int(input("Enter no of API calling threads"))) as executor:
        for location in list_of_lat_long:
            logging.debug("Thread is running.")
            latitude = str(location[0])
            longitude = str(location[1])
            response = executor.submit(client.get_reverse, latitude, longitude).result()
            output.append(response)

    print(f"{output}")    
    for i in output:
        q.put(i)
    
    
    with ThreadPoolExecutor(max_workers=int(input("Enter no of writing threads"))) as executors:
        while q.empty() is not True:
                information = q.get()
                executors.submit(filehandling,information)
    
def main():
    """
    generate log file and call function for getting information from mapquest.
    """
    logging.basicConfig(
        filename="log.log",
        style="{",
        format="{asctime} {levelname} {thread} {message}",
        level=logging.DEBUG,
    )
    client = MapQuest()
    logging.critical("Connection established with API.")
    
    information_from_mapquest_api(client)
    
if __name__ == "__main__":
    main()
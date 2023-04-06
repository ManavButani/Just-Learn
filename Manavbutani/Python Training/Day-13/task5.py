"""
All thread should also append their output data to output.json file using only single file object in previous example.
(Hint: Use locking on file object)
s
"""
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from mapquest import MapQuest
import json
import logging

def information_from_mapquest_api(client, list_of_lat_long):

    lock = Lock()
    with ThreadPoolExecutor(max_workers=len(list_of_lat_long)) as executor:
        for location in list_of_lat_long:
            logging.debug("Thread is running.")
            latitude = str(location[0])
            longitude = str(location[1])
            response = executor.submit(client.get_reverse, latitude, longitude).result()
            # print(response)
            
            filename = "output.json"
            with lock:
                with open(filename, "a") as file_pointer:
                    json.dump(response, file_pointer, indent=4)
                    file_pointer.write("\n")
            logging.info(f"{filename} is saved.")

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
    list_of_lat_long = [
        [21.1702, 72.8311],
        [23.0225, 72.5714],
        [22.3072, 73.1812],
        [21.2049, 72.8411],
        [22.6916, 72.8634],
    ]
    information_from_mapquest_api(client, list_of_lat_long)
    
if __name__ == "__main__":
    main()
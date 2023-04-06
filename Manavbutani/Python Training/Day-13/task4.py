"""
Add multithreading support for API call in handson of REST, (parsing info from Mapquest API)
a. Get latitude and longitude list from https://dpaste.com/F9VQFPJED.txt using GET call.
b. For each entry in above list get information of street, city, country, postalcode etc.
c. Store parsed information of each record in diff file. ex. Filename: <street>_<postalcode>.json
d. Add loggers in and save log in log.log file.
"""
from concurrent.futures import ThreadPoolExecutor
from mapquest import MapQuest
import json
import logging

def information_from_mapquest_api(client, list_of_lat_long):

    with ThreadPoolExecutor(max_workers=len(list_of_lat_long)) as executor:
        for location in list_of_lat_long:
            logging.debug("Thread is running.")
            latitude = str(location[0])
            longitude = str(location[1])
            response = executor.submit(client.get_reverse, latitude, longitude).result()
            # print(response)
            
            filename = response["street"] + "_" + response["postalCode"] + ".json"
            with open(filename, "w") as file_pointer:
                json.dump(response, file_pointer, indent=4)
                
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

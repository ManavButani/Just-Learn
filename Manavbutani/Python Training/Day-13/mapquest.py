import requests
class MapQuest:
    
    key="87GUw0zAbXQK0nyUCNGpywogG4mI9uhA"
    def __init__(self) -> None:
        print("Key Initialized: ")
        
    def get_address(self):
        address=input("Enter Address: ")
        g=requests.get(f"http://www.mapquestapi.com/geocoding/v1/address?key={self.key}&location={address}")
        print(g.json()["results"][0]["locations"][0]["latLng"])
        
    def post_address(self):
        address=input("Enter Address: ")
        g=requests.post(f"http://www.mapquestapi.com/geocoding/v1/address?key={self.key}&location={address}")
        print(g.json()["results"][0]["locations"][0]["latLng"])
        
    def get_reverse(self,lat,lon):
        # lat=input("Enter Latitude: ")
        # lon=input("Enter longitude: ")
        g=requests.post(f"http://www.mapquestapi.com/geocoding/v1/reverse?key={self.key}&location={lat},{lon}&includeRoadMetadata=true&includeNearestIntersection=true")
        # print(f"http://www.mapquestapi.com/geocoding/v1/reverse?key={self.key}&location={lat},{lon}&includeRoadMetadata=true&includeNearestIntersection=true")
        try:
            g=g.json()
            response_dict = {
                "street": g["results"][0]["locations"][0]["street"],
                "City": g["results"][0]["locations"][0]["adminArea3"],
                "country": g["results"][0]["locations"][0]["adminArea1"],
                "postalCode": g["results"][0]["locations"][0]["postalCode"],
            }
            
            return response_dict

        except IndexError as e:
            print("Not a valid Input")
    def get_batch(self):
        area1=input("Enter Address-1: ")
        area2=input("Enter Address-2: ")
        try:
            g=requests.post(f"http://www.mapquestapi.com/geocoding/v1/batch?key={self.key}&location={area1}&location={area2}")
            # print(g.json())
            print(g.json()["results"][0]["locations"][0]["displayLatLng"],",",g.json()["results"][1]["locations"][0]["displayLatLng"])
        except IndexError as e:
            print("Not a valid Input")
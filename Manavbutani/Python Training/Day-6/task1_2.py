"""
Write a python program using "requests" (3rd party) and "urllib3" (in-built) module to integrate "PhishTank" service.
PhishTank is a free online service, which stores information about Phishing URLs.
The Input to the program should be a URL. The output should tell us whether the input url is Phishing URL or not.
Implement a demo function which will utilize the functionality.
Input: http://www.travelswitchfly.com/
Output: "http://www.travelswitchfly.com/" is a phishing URL.
PhishTank API - https://www.phishtank.com/api_info.php
POST Endpoint - https://checkurl.phishtank.com/checkurl/index.php
"""
import json
import requests
import urllib3
def is_phishing_using_requests(url:str):
    """This function is used to check if the given link is phishing or not using requests library.
    Args:
        url (str): _description_
    """
    parameters={'url':url.encode("ascii"),'format':'json'}
    try:
        # pylint: disable-next=line-too-long
        request_object=requests.post('https://checkurl.phishtank.com/checkurl/',parameters,timeout=10)
        request_json=request_object.json()
        if request_json["meta"]["status"]=="error" :
            print(request_json["errortext"])
            print()
        elif not request_json["results"]["in_database"]:
            print("The entry is not in the PhishTank database. Try something else.")
            print()
        else:
            is_phish=request_json["results"]["valid"]
            if is_phish:
                print("This is a phishing website.")
                print(f"For more details visit: {request_json['results']['phish_detail_page']}")
                print()
            else:
                print("This link is safe.")
                print(f"For more details visit: {request_json['results']['phish_detail_page']}")
                print()
    except TimeoutError as exception:
        print(exception)
    except ValueError as exception:
        print(exception)
    except KeyError as exception:
        print(exception)
def is_phishing_using_urllib3(url:str):
    """This function is used to check if the given link is phishing or not using urllib3 library.
    Args:
        url (str): _description_
    """
    parameters={'url':url.encode("ascii"),'format':'json'}
    http = urllib3.PoolManager()
    try:
        # pylint: disable-next=line-too-long
        request_object=http.request('POST','https://checkurl.phishtank.com/checkurl/',fields=parameters,timeout=10.0)
        request_json=json.loads(request_object.data.decode('utf-8'))
        if request_json["meta"]["status"]=="error" :
            print(request_json["errortext"])
            print()
        elif not request_json["results"]["in_database"]:
            print("The entry is not in the PhishTank database. Try something else.")
            print()
        else:
            is_phish=request_json["results"]["valid"]
            if is_phish:
                print("This is a phishing website.")
                print(f"For more details visit: {request_json['results']['phish_detail_page']}")
                print()
            else:
                print("This link is safe.")
                print(f"For more details visit: {request_json['results']['phish_detail_page']}")
                print()
    except TimeoutError as exception:
        print(exception)
    except ValueError as exception:
        print(exception)
    except KeyError as exception:
        print(exception)
while True:
    print("Welcome to PhishTank!!")
    print("1: Enter url to check if it is phishing or not using requests:")
    print("2: Enter url to check if it is phishing or not using urllib3:")
    print("3: To exit the application:")
    choice=int(input("Enter your choice:"))
    print()
    if choice==1:
        url_to_check=input("Enter the url to check:")
        is_phishing_using_requests(url_to_check)
    elif choice==2:
        url_to_check=input("Enter the url to check:")
        is_phishing_using_urllib3(url_to_check)    
    elif choice==3:
        break
    else:
        print("Invalid Input")
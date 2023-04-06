"""
Write unit tests for the Phishtank exercise form REST API session. 
Use mocking to mock any API calls that need to be made.
"""
import requests
def phishing(url:str):
    """This function is used to check if the given link is phishing or not using requests library.

    Args:
        url (str): _description_
    """
    parameters={'url':url.encode("ascii"),'format':'json'}
    try:
        # pylint: disable-next=line-too-long
        request_object=requests.post('https://checkurl.phishtank.com/checkurl/',parameters,timeout=10)
        print(request_object)
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

def main(url="gg"):
    return phishing(url)

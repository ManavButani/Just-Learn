import requests

p = {"n": input("Enter URL: ")}
p=requests.get("http://127.0.0.1:5000/"+str(p))
print("This url is not valid", p.json()["valid"])
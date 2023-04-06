from flask import Flask,  render_template,  request
import pandas as pd
import requests

app = Flask(__name__)
@app.route("/")
def home_():
    return render_template("index.html")

@app.route("/result",methods=['POST','GET'])
def res():
    if request.method == "GET":
        return render_template("result.html")
    elif request.method == 'POST':
        manas=request.form["identity"]
        k=requests.post(f"http://127.0.0.1:5000/check/{int(manas)}")
        try:
            z=k.json()
        except Exception as e:
            return "<h1>Please enter valid ID no<h1>"
        if z["valid"]=="YES":
            df = pd.read_csv("result.csv")
            id = z["count"]
            m=df[df.ID==id]["CGPA"][id-1]
            return "<h3>Your current CGPA is </h3><h1>"+str(m)+"</h1>"
        else:
            return "<h1>Pay Your Fees First</h1>"

if __name__ == "__main__":
    app.run(debug=True,port=5001)
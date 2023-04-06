from flask import Flask, jsonify, render_template, url_for, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fees",methods=['POST','GET'])
def fees():
    if request.method == "GET":
        return render_template("fees.html",result={})
    else:
        manas=request.form["identity"]
        return redirect(url_for('fee',id=manas))

@app.route("/fees/<int:id>")
def fee(id):
    df=pd.read_csv('fees.csv')
    if id in df['ID']:
        x=df[df.ID==id]["STATUS"][id-1]
        result = {
            'valid': x
        }
        return render_template("fees.html",result=result)
    else:
        return "<h1>Please enter valid ID no<h1>"
    
@app.route("/check/<int:id>",methods=["POST"])
def fee_(id):
    df=pd.read_csv('fees.csv')
    if id in df['ID']:
        x=df[df.ID==id]["STATUS"][id-1]
        y=df[df.ID==id]["ID"][id-1]
        result = {
            'valid': x,
            'count': int(y)
        }
        return result
    else:
        return "<h1>Please enter valid ID no<h1>"

if __name__ == "__main__":
    app.run(debug=True)
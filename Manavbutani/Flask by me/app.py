from flask import Flask, render_template, url_for, request
import requests
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        lastname = request.form["lastname"]
        firstname = request.form["firstname"]
        country = request.form["country"]
        subject = request.form["subject"]
        return render_template("greeting.html", firstname=firstname, lastname=lastname, country=country, subject=subject)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
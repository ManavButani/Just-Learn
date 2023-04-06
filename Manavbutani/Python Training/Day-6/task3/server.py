from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/<string:n>",methods=['GET'])
def isvalid(n):
    data = pd.read_csv("data.csv")
    for i in range(len(data["url"])):
        if n in data["url"][i] and data["isvalid"][i]=="yes":
            result = {
                "url": data["url"][i],
                "valid" : "Yes"}
            return jsonify(result)
        else:
            result = {
                "valid": "No"}
            return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
import requests
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

color = "#16a085"

@app.route("/")
def hello():

    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    querystring = {"lon":"38.5","lat":"-78.5"}
    headers = {
        'x-rapidapi-key': "8a57e07b59msh02957c12032341dp1fd5c7jsn224ad21c34c3",
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

    return render_template('index.html', contents=response.text, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)

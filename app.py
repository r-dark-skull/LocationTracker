from flask import Flask, request
import requests

app = Flask(__name__)

def get_geolocation(ip):
    resp = requests.get(f'http://ip-api.com/json/{ip}')
    print(resp)

@app.route("/")
def homepage():
    get_geolocation(request.remote_addr)
    return open("./static/index.html").read()

@app.route("/script.js")
def js_script():
    return open("./static/script.js").read()

@app.route("/name=<params>")
def name(params):
    print(request.remote_addr, params)
    return "<h1>Page home </h1>"


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
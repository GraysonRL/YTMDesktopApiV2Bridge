import flask
import requests as req
from flask import request 
import random
import secrets
import jstyleson
import time
from flask_cors import CORS
currentcode=0

with open("config.json", 'r') as f:
    z=(jstyleson.loads(f.read()))

print(z)
app = flask.Flask(__name__)
CORS(app)
#OPTIONS /api/v1/auth/requestcode HTTP/1.1"
@app.route('/')
def home():
    return "kill yourse;lf"
@app.route('/api/v1/auth/requestcode',methods=["POST","OPTIONS"])
def requestcode():
    print(request.method)
    print(request.__dict__)
    currentcode=random.randint(1000,9999)
    return {"code":currentcode}
@app.route('/api/v1/auth/request',methods=["POST","OPTIONS"])
def authreq():
    Z=secrets.token_hex(1024)
    print(Z)
    with open('token', 'w') as f:
        f.write(f"{Z}") #no idea if this is secure (99% sure it isnt) but this bridge is already just not good at all so we ball
    return {"token":Z}
app.run(z["BridgeHost"], port=z["BridgePort"])
# TODO:
# Implement the Websocket
#       127.0.0.1 - - [08/Feb/2025 22:05:46] "GET /socket.io/?EIO=4&transport=websocket HTTP/1.1" 404 -
# also implement everything else from https://github.com/ytmdesktop/ytmdesktop/wiki/v2-%E2%80%90-Companion-Server-API-v1 except for auth 😭
# Actually connect the features to the endpoints shown at http://localhost:26538/swagger
# Add GUI ? Kinda pointless but maybe
# Create TH-CH youtube plugin that auto-runs this script or even better runs this in naitive TS/JS
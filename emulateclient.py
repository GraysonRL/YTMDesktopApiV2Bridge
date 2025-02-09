import requests
import json
##Used to pretend to be the craftify auth page
##Very low quality, barely works, and was only used for development
appId="craftify"
headers={
     "Content-Type": "application/json"
}
data={
    "appId": appId,
        "appName": "Craftify2",
        "appVersion": "1.0.1"
}
z=requests.post('http://localhost:9863/api/v1/auth/requestcode',headers=headers,json=data)
print(data)
print(z)
print(z.text)
print(z.status_code)
print(z.raw)
print(z.content)
code=json.loads(z.text)["code"]
data={
    "appId": appId,
    "code": code
}
a=requests.post("http://localhost:9863/api/v1/auth/request",headers=headers,json=data)
print(a)
token=json.loads(a.text)["token"]
print(a.text)
print(a.status_code)
print(a.raw)
print(a.content)
print(token)
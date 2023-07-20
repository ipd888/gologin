import requests
import json

url = "https://api.gologin.com/browser"

payload = json.dumps({
  "name": "string",
  "notes": "string",
  "browserType": "chrome",
  "os": "lin",
  "startUrl": "string",
  "googleServicesEnabled": False,
  "lockEnabled": False,
  "debugMode": False,
  "navigator": {
    "userAgent": "string",
    "resolution": "string",
    "language": "string",
    "platform": "string",
    "doNotTrack": False,
    "hardwareConcurrency": 0,
    "deviceMemory": 1,
    "maxTouchPoints": 0
  },
  "geoProxyInfo": {},
  "storage": {
    "local": True,
    "extensions": True,
    "bookmarks": True,
    "history": True,
    "passwords": True,
    "session": True
  },
  "proxyEnabled": False,
  "proxy": {
    "mode": "http",
    "host": "string",
    "port": 0,
    "username": "string",
    "password": "string"
  },
  "dns": "string",
  "plugins": {
    "enableVulnerable": True,
    "enableFlash": True
  },
  "timezone": {
    "enabled": True,
    "fillBasedOnIp": True,
    "timezone": "string"
  },
  "audioContext": {
    "mode": "off",
    "noise": 0
  },
  "canvas": {
    "mode": "off",
    "noise": 0
  },
  "fonts": {
    "families": [
      "string"
    ],
    "enableMasking": True,
    "enableDomRect": True
  },
  "mediaDevices": {
    "videoInputs": 0,
    "audioInputs": 0,
    "audioOutputs": 0,
    "enableMasking": False
  },
  "webRTC": {
    "mode": "alerted",
    "enabled": True,
    "customize": True,
    "localIpMasking": False,
    "fillBasedOnIp": True,
    "publicIp": "string",
    "localIps": [
      "string"
    ]
  },
  "webGL": {
    "mode": "noise",
    "getClientRectsNoise": 0,
    "noise": 0
  },
  "clientRects": {
    "mode": "noise",
    "noise": 0
  },
  "webGLMetadata": {
    "mode": "mask",
    "vendor": "string",
    "renderer": "string"
  },
  "webglParams": [],
  "profile": "string",
  "googleClientId": "string",
  "updateExtensions": True,
  "chromeExtensions": [
    "string"
  ]
})
headers = {
  'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGI1MjkzNDBjNGE0OWQ4NmRkNWZjYTciLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGI1MmM4Mzc0ZjUyNDc3YTJkZGY5ZjgifQ.AqUkAwhhEuSTryypsG_i7PChKaBghWyL2oOnilQCwoU',
  'Content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

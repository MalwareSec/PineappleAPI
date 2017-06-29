#Python 2.7
import requests,json
API_TOKEN="50799856e16e97bb126fa390ab9c7a44790d2dbf16e2f684186351c3ecbe1ab76f5112f53f1c782d81d5bf75ca1ac3c3370d2cffbf3560278b1391ea9c8bc339"

payload={
	"module":"PineAP",
	"action":"setPineAPSettings",
	"settings":{"allowAssociations":"true", "logProbes":"true", "logAssociations":"true"},
	"allowAssociations":"True",
	"apiToken":API_TOKEN
}

resp = requests.post("http://172.16.42.1:1471/api/",data=json.dumps(payload))

print resp.text

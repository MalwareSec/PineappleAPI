#Python 2.7
import requests,json
#API token from API token module
API_TOKEN= raw_input("Enter your API Token: ")
payload={
	"module":"PineAP",
	"action":"setPineAPSettings",
	"settings":{"allowAssociations":"true", "logProbes":"true", "logAssociations":"true"},
	"allowAssociations":"True",
	"apiToken":API_TOKEN
}

resp = requests.post("http://172.16.42.1:1471/api/",data=json.dumps(payload))

print resp.text

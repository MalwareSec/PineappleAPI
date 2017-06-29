#Python 2.7
import requests, json
API_TOKEN=raw_input("Enter the API Token: ")
payload = {
	"module":"Clients",
	"action":"getClientData",
	"apiToken": API_TOKEN
}


resp = requests.post("http://172.16.42.1:1471/api/", data=json.dumps(payload))
print resp.text
#print resp.json()


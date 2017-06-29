#Python 2.7
import requests, json
API_TOKEN="9d4e67f06446d7c4166c555b6ec6697706d054a1d04407dbfa1d69ea85f848af7dbf5316623da0adde4e697102040df8937f0b37efb174c0cccc7b4b6651fd13"
payload = {
	"module":"Clients",
	"action":"getClientData",
	"apiToken": API_TOKEN
}


resp = requests.post("http://172.16.42.1:1471/api/", data=json.dumps(payload))
print resp.text
#print resp.json()


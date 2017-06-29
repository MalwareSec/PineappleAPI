#Python 2.7
import requests, json

#API token from token module
API_TOKEN = raw_input("Enter the API Token: ")
payload = {
	"module":"Logging",
	"action":"getPineapLog",
	"apiToken": API_TOKEN
}

resp = requests.post("http://172.16.42.1:1471/api/", data=json.dumps(payload))
print resp
print resp.json()

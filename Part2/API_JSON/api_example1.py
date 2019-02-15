import requests
import json

# GET API HERE http://www.omdbapi.com/apikey.aspx
# GET API key from api_keys.json
with open("./Part2/API_JSON/api_keys.json") as json_file:
    json_data = json.load(json_file)

api_key = json_data['api_key_omdb']

url = 'http://www.omdbapi.com/?t=hackers&apikey=' + api_key 

r = requests.get(url)

json_data = r.json()

for key, value in json_data.items():
    print(key + ':', value)



import requests
import json

# GET API HERE http://www.omdbapi.com/apikey.aspx
# GET API key from api_keys.json
with open("./Part2/API_JSON/api_keys.json") as json_file:
    json_data = json.load(json_file)

api_key = json_data['api_key_omdb']

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?t=the+social+network&apikey=' + api_key

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


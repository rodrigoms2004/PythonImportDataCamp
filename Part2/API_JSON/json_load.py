import json

with open('./Part2/API_JSON/snakes.json', 'r') as json_file:
    json_data = json.load(json_file)
                

print(type(json_data))
print(json_data)

for key, value in json_data.items():
        print(key + ':' + value)


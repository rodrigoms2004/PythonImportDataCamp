import json


with open("./Part2/API_JSON/a_movie.json") as json_file:
    json_data = json.load(json_file)


print(json_data['Title'])
print(json_data['Year'])
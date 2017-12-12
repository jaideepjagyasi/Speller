import requests as r
import json
response = r.get("http://api.pearson.com/v2/dictionaries/entries?headword=a")
json_response=json.loads(response.text)
print(len(json_response["results"]))

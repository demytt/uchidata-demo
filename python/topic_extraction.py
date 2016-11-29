import json
import requests

myKey = "your_api_key"
uchidata_url = "url_to_request"
model = "topic-extraction"

# Prepare data for the request
d = {'key':myKey}
d['model'] = model
d['observations'] = []
d['observations'].append({'id':'1', 'content':'Champions League: Football and politics unite Celtic and Barcelona fans'})
d['observations'].append({'id':'2', 'content':'A number of popular websites like Twitter and Netflix went down for some users on Friday in a massive cyberattack with international reach'})

# Send request
result = requests.get(uchidata_url + '/getPredictions', data=json.dumps(d))

# Print result
try:
    result_json = json.loads(result.content)
    print(json.dumps(result_json, indent=2, sort_keys=True))
except Exception,e: 
    print "Error : " + str(result.content)


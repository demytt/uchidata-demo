import json
import requests

myKey = "your_api_key"
uchidata_url = "url_to_request"
model = "sentiment-analysis"

# Prepare data for the request
d = {'key':myKey}
d['model'] = model
d['observations'] = []
d['observations'].append({'id':'1', 'content':'Data scientist is an awesome job ! I really like what I do :)'})
d['observations'].append({'id':'2', 'content':'Some people are so weird, they listen boring music everyday !'})

# Send request
result = requests.get(uchidata_url + '/getPredictions', data=json.dumps(d))

# Print result
try:
    result_json = json.loads(result.content)
    print(json.dumps(result_json, indent=2, sort_keys=True))
except Exception,e: 
    print "Error : " + str(result.content)


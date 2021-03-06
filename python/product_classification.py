import json
import requests

myKey = "your_api_key"
uchidata_url = "url_to_request"
model = "product-classification"

# Prepare data for the request
d = {'key':myKey}
d['model'] = model
d['observations'] = []
d['observations'].append({'id':'1', 'content':'Acer K132 1280 x 800 WXGA 600 ANSI Lumens 16:10 Aspect Ratio  HDMI / MHL Input '})

# Send request
result = requests.get(uchidata_url + '/getPredictions', data=json.dumps(d))

# Print result
try:
    result_json = json.loads(result.content)
    print(json.dumps(result_json, indent=2, sort_keys=True))
except Exception,e: 
    print "Error : " + str(result.content)


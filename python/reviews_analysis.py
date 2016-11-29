import json
import requests

myKey = "your_api_key"
uchidata_url = "url_to_request"
model = "reviews-analysis"

# Prepare data for the request
d = {'key':myKey}
d['model'] = model
d['observations'] = []
d['observations'].append({'id':'1', 'content':"If you are want Bluetooth headphones, don't pass them up. These Bluetooth headphones are amazing for $35. They claim 57mm size drivers which are quite large and they definitely have a big sound. The battery is amazing so far. I received it right before taking it on a trip. I flew and they were great on the plane."})
d['observations'].append({'id':'2', 'content':'This is a book explaining classic American food in a somewhat scientific manner. There are no fancy foreign dishes in the book. Even the French quiche lorraine gets the American treatment'})

# Send request
result = requests.get(uchidata_url + '/getPredictions', data=json.dumps(d))

# Print result
result_json = json.loads(result.content)

try:
    result_json = json.loads(r.content)
    print(json.dumps(result_json, indent=2, sort_keys=True))
except Exception,e: 
    print "Error : " + str(r.content)




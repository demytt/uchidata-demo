# Welcome on Uchidata SDK for python developpers #

This README will explain you how to send request to Uchidata API.

Every request must have the following structure :

{
  'key':XXX
  'model':"XXX"
  'observations' = [{'id':1, 'content':'XXX'}, {'id':2, 'content':'YYY'}, {'id':3, 'content':'ZZZ'}]
}

Where :
  - key = your API key. If you don't have access to the demo, feel free to ask on uchidata.com
  - model = the model to request. Accepted values : "sentiment", "review", "topic", "product-classification"
  - maximum number of observations per request : 10

Please send the request to the url specified when you ask for a free access on uchidata.com


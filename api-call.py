import requests
import json

#Note: Query string accepts quotes and advanced operators.
key ='ENTER-API-KEY-HERE'
qstring = 'ENTER-SEARCH-QUERY-STRING'

url = 'https://www.googleapis.com/customsearch/v1'
params = {'key': key,
		  'cx': '014319016878028384416:9smkfccp77w',
		  'q': qstring}

r = requests.get(url, params=params)

#Tell me if something goes wrong:
r.raise_for_status()

#USER INPUT HERE:
#Save the results to json file:
with open('CREATE-FILENAME-HERE', 'w') as outfile:
    json.dump(r.json(), outfile)

#Review the request url:
print(r.url)
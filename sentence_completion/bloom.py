import requests
from pprint import pprint

API_URL = 'https://api-inference.huggingface.co/models/bigscience/bloom'
TOKEN = "Bearer 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"
headers = {'Authorization': TOKEN}
# The Entertheaccesskeyhere is just a placeholder, which can be changed according to the user's access key

# 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
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
  
params = {'max_length': 200, 'top_k': 10, 'temperature': 2.5}
output = query({
    'inputs': 'Cricket is a',
    'parameters': params,
})

pprint(output)
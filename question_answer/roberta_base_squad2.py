
import requests
from pprint import pprint
API_URL = 'https://api-inference.huggingface.co/models/deepset/roberta-base-squad2'
TOKEN = "Bearer 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"

headers = {'Authorization': TOKEN}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
  
params = {'max_length': 200, 'top_k': 10, 'temperature': 2.5}
output = query({
    'inputs': {
            "question": "What's my profession?",
            "context": "My name is Suvojit and I am a Senior Data Scientist"
        },
    'parameters': params
})

pprint(output)
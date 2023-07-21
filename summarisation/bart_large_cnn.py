
import requests
from pprint import pprint
TOKEN = "Bearer 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"
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {'Authorization': TOKEN}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
    
params = {'do_sample': False}

full_text = '''AI applications are summarizing articles, writing stories and 
engaging in long conversations — and large language models are doing 
the heavy lifting.

A large language model, or LLM, is a deep learning model that can 
understand, learn, summarize, translate, predict, and generate text and other 
content based on knowledge gained from massive datasets.

Large language models - successful applications of 
transformer models. They aren’t just for teaching AIs human languages, 
but for understanding proteins, writing software code, and much, much more.

In addition to accelerating natural language processing applications — 
like translation, chatbots, and AI assistants — large language models are 
used in healthcare, software development, and use cases in many other fields.'''

output = query({
    'inputs': full_text,
    'parameters': params
})

pprint(output)
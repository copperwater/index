from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

# url = 'http://localhost:5350/crawling'
# data = {'urls': 'http://google.com/'}

# request = Request(url)
# response = urlopen(request, json.dumps(data).encode('utf-8')).read()
# print(str(response))

#url = 'http://localhost:5432/text_Transformation'
url = 'http://localhost:5350/text_Transformation'

data = {
    "metadata": {
        "charset": "UTF-8",
        "title": "TextTransformation",
        "url": "indigoO.cs.rpi.edu",
        "timestamp": "2018-11-15T16:25:56+00:00",
        "keywords": [],
        "description": [],
        "docid": 3
    },
    "ngrams": {
        "all": {
            "1grams": {
                "TextTransformation": 1,
                "hello": 1,
                "world": 1,
                "the": 1,
                "end": 1
            },
            "2grams": {
                "tom brady": 5
            }
        },
        "headers":
        {
            "1grams": {
                "hello": 1,
                "world": 1
            },
            "2grams": {
                "what is": 1
            }
        },
        "title": {
            "1grams": {
                "TextTransformation": 1
            },
            "2grams": {
                "texty texty": 2
            }
        }
    }
}

request = Request(url)
response = urlopen(request, json.dumps(data).encode('utf-8')).read()
print(str(response))

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

url = 'http://localhost:5350/crawling'
data = {'urls': 'http://google.com/'}

request = Request(url)
response = urlopen(request, json.dumps(data).encode('utf-8')).read()
print(str(response))

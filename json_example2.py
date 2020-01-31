import json
from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/posts") as response:
    source = response.read()

data = json.loads(source)

for d in data:
    print(d['userId'])
    print(d['id'])
    print(d['title'])
    print(d['body'])
    print()

# print(json.dumps(data, indent=2))
import requests

r = requests.get('https://xkcd.com/353/')

print(dir(r))
#print(help(r))

print(r.text)

r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.content)

with open('image.png', 'wb') as f:
    f.write(r.content)
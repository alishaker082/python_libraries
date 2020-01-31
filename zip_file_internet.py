import requests
import zipfile

r = requests.get("https://github.com/CoreyMSchafer/dotfiles/archive/master.zip")

with open('data.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
    data_zip.extractall()

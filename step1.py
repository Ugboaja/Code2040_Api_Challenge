import requests  
import json

apitoken = "0d45ff4863bcc8ba0a73e4216aa4aab8"
githublink = "https://github.com/Ugboaja/Code2040_Api_Challenge"

data = {'token': apitoken, 'github': githublink}
r = requests.post("http://challenge.code2040.org/api/register", data)
print r


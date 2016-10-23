import requests  
import json

data = {'token':'0d45ff4863bcc8ba0a73e4216aa4aab8'}
r = requests.post("http://challenge.code2040.org/api/haystack", data)
print r.json()
jsonData = str(r.text)
d = json.loads(jsonData)
def linearsearch():
    for i in xrange(len(d["haystack"])):
        if d["needle"] == d["haystack"][i]:
            x = i
    return x
result = linearsearch()
data2 = {'token':'0d45ff4863bcc8ba0a73e4216aa4aab8', 'needle': result}
r2 = requests.post("http://challenge.code2040.org/api/haystack/validate", data2)

print r2.status_code
print r2.text

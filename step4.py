import requests  
import json

data = {'token': '0d45ff4863bcc8ba0a73e4216aa4aab8'}
r = requests.post("http://challenge.code2040.org/api/prefix", data)
print r.json()
print r.status_code
pre = r.json()["prefix"]
arr = r.json()["array"]
def prefix(prefix, array):
    newarray = []
    for i in xrange(len(array)):
        if array[i][0:len(pre)] != pre:
            newarray.append(array[i])
    return newarray

result = prefix(pre,arr)
print result
data1 = {'token': '0d45ff4863bcc8ba0a73e4216aa4aab8','array': result}
url = "http://challenge.code2040.org/api/prefix/validate"
r1 = requests.post(url, json=data1)
print r1


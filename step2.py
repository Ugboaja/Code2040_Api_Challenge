import requests  
import json

data = {'token':'0d45ff4863bcc8ba0a73e4216aa4aab8'}
dat = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/reverse", data)
print dat
print r.text
print r.status_code 

def reverse(string):
	return string[::-1]
    
result = reverse(r.text)
print result
data2 = {'token': '0d45ff4863bcc8ba0a73e4216aa4aab8', 'string': result}
r2= requests.post('http://challenge.code2040.org/api/reverse/validate', data2)
print r2.text
print r2.status_code 


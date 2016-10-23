import requests  
import json
import dateutil.parser
import datetime
import iso8601

data = {'token':'0d45ff4863bcc8ba0a73e4216aa4aab8'}
r = requests.post('http://challenge.code2040.org/api/dating', data)
print r.json()
jsonData = r.json()
thedate = jsonData['datestamp']
theinterval = jsonData['interval']
def datestamp(interval, thedate):
	interval = int(interval)
	date = iso8601.parse_date(thedate)
	interval = datetime.timedelta(0, interval)
	final = date + interval
	final = final.isoformat()
	format1 = final.split('+')[0]
	format1 += 'Z'
	return format1
result = datestamp(theinterval, thedate)
print result

data3 = {'token': '0d45ff4863bcc8ba0a73e4216aa4aab8', 'datestamp': result}
r3 = requests.post('http://challenge.code2040.org/api/dating/validate', data3)
print r3.status_code


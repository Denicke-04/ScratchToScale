import requests
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
data = {'url':'https://bit.ly/hat-test'}
results = requests.post(url,json = data)
print(results.text)
import requests
url = 'http://localhost:9600/predict'
data = {'url':'https://bit.ly/hat-test'}
results = requests.post(url,json = data)
print(results.text)
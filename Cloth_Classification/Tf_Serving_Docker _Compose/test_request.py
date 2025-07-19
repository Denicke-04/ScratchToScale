import requests
url = 'http://localhost:9600/predict'
data = {'url':'https://bit.ly/pants-test'}
results = requests.post(url,json = data)
print(results.text)
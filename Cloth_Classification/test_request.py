import requests
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
#url = 'https://nuupb201g1.execute-api.eu-west-1.amazonaws.com/cloth-classification-test/classify' ##aws url
data = {'url':'https://bit.ly/hat-test'}
results = requests.post(url,json = data)
print(results.text)
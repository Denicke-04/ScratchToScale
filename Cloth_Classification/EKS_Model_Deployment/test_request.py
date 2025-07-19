import requests
url = 'http://localhost:9600/predict'
#url = 'http://a6f24826ba1cb4922bf35c74a1ce3253-102749770.eu-west-1.elb.amazonaws.com/predict' ## EKS URL
data = {'url':'https://bit.ly/pants-test'}
results = requests.post(url,json = data)
print(results.text)
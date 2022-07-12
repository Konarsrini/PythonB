import requests

url = 'https://www.skillsugar.com/examples/json/example_1.json'

result = requests.get(url)
print(result.text)
print(result.headers)
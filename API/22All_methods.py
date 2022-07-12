import requests

url = 'https://www.skillsugar.com/examples/json/example_1.json'

result = requests.get(url)
result.encoding - the encoding that the document is using (UTF-8 .etc)
result.headers - the response headers in JSON format
result.cookies - the request cookies
result.status_code - the status of the response in a code format (200, 500, 404 .etc.)
result.content - the content of the response in binary format
result.text - the decoded content of the response according to the response encoding header property
result.is_redirect - True if the response status code is a redirect, False if not
result.elapsed - the time between sending the request and getting a response
result.url - the URL of the request
result.json() - parse JSON content
---------------------------
import requests

url = 'https://www.skillsugar.com/search'

params = {'query': 'python', 'sort': 'date'}

result = requests.get(url, params=params)

print(result.url)
https://www.skillsugar.com/search?query=python&sort=date
-------------------------------
import requests

url = 'https://www.skillsugar.com/contact'

params = {'name': 'john', 'subject' : 'Test', 'message': 'Hello', 'email': 'john@skillsugar.com'}

result = requests.post(url, params=params)

print(result.headers)
-------------------------------
result = requests.put('https://www.skillsugar.com/put', data = {'key':'value'})
-------------------------------
result = requests.patch('https://www.skillsugar.com/patch', params = {'key':'value'})
-------------------------------
result = requests.delete('https://www.skillsugar.com/delete', params = {'key':'value'})
-------------------------------

-------------------------------

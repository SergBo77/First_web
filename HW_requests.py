import requests
import pprint

# ЗАДАНИЕ 1
params = {
          'q': 'html'
         }
response = requests.get('https://api.github.com', params=params)
print(response.status_code)
response_json = response.json()
pprint.pprint(response_json)

# ЗАДАНИЕ 2
params_1 = {
          'userId': 1
         }
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params_1)
print(response.status_code)
response_json = response.json()
pprint.pprint(response_json)

# ЗАДАНИЕ 3

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
       'title': 'foo',
       'body': 'bar',
       'userId' : 1
        }
response_p = requests.post(url, data=data)
print(response_p.status_code)
print (f'ответ - {response_p.json()}')
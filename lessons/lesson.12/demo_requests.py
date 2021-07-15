from pprint import pprint

import requests

params = {"foo": "bar", "spam": "eggs"}
response = requests.get("http://httpbin.org/get", params=params)

print(response)
pprint(response.json())

json = {"foo": "bar", "spam": "eggs", "user_ids": [1, 2, 3]}
response = requests.post("http://httpbin.org/post", json=json)

print(response)
pprint(response.json())

resp_err = requests.get("http://httpbin.org/status/504")
print(resp_err)
print(resp_err.status_code)

import requests

data = requests.get("http://google.com").text
print(data)

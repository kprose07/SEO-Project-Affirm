from pip._vendor import requests
url = "https://affirmations.dev/"
r = requests.get(url)
print(r.status_code)
print(r.json())
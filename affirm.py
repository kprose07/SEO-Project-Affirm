from pip._vendor import requests
url = "https://affirmations.dev/"
r = requests.get(url)
dict = r.json()
affirm = dict.get('affirmation')
print(r.status_code)
for i in range(0,7):
    print(affirm)

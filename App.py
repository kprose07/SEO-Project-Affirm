from pip._vendor import requests
limit = 10
category = 'hope'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'x9mA4K+qggViRYlpXcn0TQ==NfEF6hREqofCMMqd'})
rdict = response.json()
quote = rdict[0].get('quote')
if response.status_code == requests.codes.ok:
    
    print(rdict)
    
    save = input("Would you like to save this quote? (Y or N) ")
    if save == "Y" or save == "y":
        print( "quote saved")
    else:
        print("OK BYE!")
else:
    print("Error:", response.status_code, response.text)
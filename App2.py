import requests
import pymysql
import os

#GET API Key
APIKey = os.environ.get('APIKEY')

# API Data
limit = 10
category = 'hope'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': APIKey})
rdict = response.json()
quote = rdict[0].get('quote')
author = rdict[0].get('author')
category = rdict[0].get('category')

#remove special characters
quote= "".join(ch for ch in quote if ch.isalnum() or ch.isspace())
author="".join(ch for ch in author if ch.isalnum()or ch.isspace())
category="".join(ch for ch in category if ch.isalnum()or ch.isspace())


# SQL SETUP (MARIA)
Host = "localhost"  
User = "root"       
Password = "codio"           
Database = "quotes"

#Insert Data
conn  = pymysql.connect(host=Host, user=User, password=Password, database=Database)
cur  = conn.cursor()
query = f"INSERT INTO myquotesdata (Quote,Author,Category) VALUES ('{quote}','{author}','{category}')"

#Read Data
check = cur.execute("SELECT * FROM myquotesdata")

  
# fetch all the matching rows 
def viewSavedQuotes():
    if check:
        cur.execute("SELECT * FROM myquotesdata")
        result = cur.fetchall()
        for row in result:
            print(row)
            print("\n")

#App Logic
if response.status_code == requests.codes.ok:
    print('Topic: '+category+'\n'+'Written By: ' +author+'\n'+'"'+quote+'"')
    save = input("Press Y to Save Quote, Press V to View, or Press N to exit. ")
    if save == "Y" or save == "y":
        cur.execute(query)
        conn.commit()
        conn.close()
        print( "quote saved")
    elif save == "V" or "v":
        viewSavedQuotes()

    else:
        print("OK! See you tommorrow!")
else:
    print("Error: SERVER IS DOWN: ", response.status_code, response.text)
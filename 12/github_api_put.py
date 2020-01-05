import requests, json

with open('token.txt') as file_:
    token = file_.read().strip()

#Setting header of the request so we are able to access the data in the profile 
headers = {'Authorization' : 'token ' + token}

page = requests.put('https://api.github.com/user/starred/pyvec/naucse.python.cz', headers=headers)
page.raise_for_status()

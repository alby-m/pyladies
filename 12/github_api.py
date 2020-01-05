import requests, json

with open('token.txt') as file_:
    token = file_.read().strip()

#Setting header of the request so we are able to access the data in the profile 
headers = {'Authorization' : 'token ' + token}

page = requests.get('https://api.github.com/user', headers=headers)
page.raise_for_status()
print(page.text)

#Make it JSON 
data = json.loads(page.text)

#Pretty print it
print(json.dumps(data, ensure_ascii=True, indent=2))

#Pull some key from it
print(data['avatar_url'])
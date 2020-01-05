import requests

#downloading the page
page = requests.get('https://github.com')

#check if request was done ok
page.raise_for_status()

#printing the content of the page 
print(page.text)
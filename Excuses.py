import requests
import json

print("Are you tired of thinking about a new excuse? We can help you!")
categories = input("Where you don't want to go? (office/family/children/college/party): ")

howMany = input("How many excuses you need? (number): ")

if howMany == '1':
  response = requests.get(f'https://excuser.herokuapp.com/v1/excuse/{categories}')
else:
  response = requests.get(f'https://excuser.herokuapp.com/v1/excuse/{categories}/{howMany}')


if (response.status_code != requests.codes.ok):
  print("Something is wrong")
else:
  print(json.dumps(response.json() , indent=5))
  

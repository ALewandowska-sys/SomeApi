import requests
import json

print("Are you tired of thinking about a new excuse? We can help you!")
categories = input("Choose for who you need a random exuce (office/family/children/college/party): ")

howMany = input("Only one excuse you need? (no/number): ")

if howMany == 'no':
  response = requests.get(f'https://excuser.herokuapp.com/v1/excuse/{categories}')
else:
  response = requests.get(f'https://excuser.herokuapp.com/v1/excuse/{categories}/{howMany}')


if (response.status_code != requests.codes.ok):
  print("Something is wrong")
else:
  print(json.dumps(response.json() , indent=5))
  

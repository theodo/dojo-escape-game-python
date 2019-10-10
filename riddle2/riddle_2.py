import json

FILE_NAME = './addresses.json'

with open(FILE_NAME) as json_file:
    data = json.load(json_file)
    
    print(data['myUser-123'])
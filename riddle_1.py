import requests

BASE_URI = "http://ripper.theo.do"

ENDPOINT = "/api/get-username"
ID = "/316"  # A remplacer avec son ID
URL = BASE_URI + ENDPOINT + ID

response = requests.get(URL)

data = response.content.decode()

print(data)

import requests 
  
BASE_URI = "http://ripper.theo.do"

# A Compléter
ENDPOINT = ""
ID = ""
URL = BASE_URI + ENDPOINT + ID

response = requests.get(url=URL) 
  
# extracting data in json format 
data = response.json()
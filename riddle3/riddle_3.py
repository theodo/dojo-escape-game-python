import requests


BASE_URI = "http://ripper.theo.do"

ENDPOINT = "/api/auth/jwt/create"
MY_USER_NAME = ""
MY_PASSWORD = ""

payload = {"username": MY_USER_NAME, "password": MY_PASSWORD}

response = requests.post(url=BASE_URI + ENDPOINT, data=payload)

data = response.content.decode()

print(data)

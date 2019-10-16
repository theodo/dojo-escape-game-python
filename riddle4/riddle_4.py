import requests
from flask import Flask

app = Flask(__name__)

SERVER_MOUNTER_URL = "http://ripper.theo.do/api/server-mounted"


@app.route("/")
def server_successfully_mounted():
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxMjM1NDYxLCJqdGkiOiJmYmI3OWY0MTNkNWQ0ZDQ1OTUzMzNjYjgzMDE4OGNiOCIsInVzZXJfaWQiOjE0NH0.5PzBmcLonuvMS9s9s7pjxte_zc3uf1pDFCL9LK3dZIc"  # A remplacer
    ip_address = "10.231.165.12"  # A remplacer

    return requests.post(
        SERVER_MOUNTER_URL,
        data={"ip_address": ip_address},
        headers={"Authorization": "Bearer {}".format(token)},
    ).content.decode()


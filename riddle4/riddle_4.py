import requests
from flask import Flask

app = Flask(__name__)

SERVER_MOUNTER_URL = "http://ripper.theo.do/api/server-mounted"


@app.route("/")
def server_successfully_mounted():
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwbGF5ZXJfaWQiOjY4LCJ1c2VybmFtZSI6ImNvbXBhY3RfY2hyaXN0YWJlbGxhIn0.Rkiq8A3T1ywW19WEM8dgVt6Ro2LoDj3bvhGRAL1LX0M"  # A remplacer
    ip_address = "10.231.165.12"  # A remplacer

    return requests.post(
        SERVER_MOUNTER_URL, data={"token": token, "ip_address": ip_address}
    ).content.decode()


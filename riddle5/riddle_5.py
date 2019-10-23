import requests
import json

# Get culprit name from spotify API
HINT_URL = "https://api.spotify.com/v1/playlists"
culprit_playlist_id = "4wRfyALTv1jNL7HScIhd1S"
spotify_token = "BQCnevGOQcUclx-zbEg4DRZXPLmE4o2y1I135ZlRRgMHsK0y3oElz3d8ySXmS-afU8rUtmgM0rGj6BqVlAY_6jPcXkKIwN2um3ZwVINEXpDGohZWrDnFoG3eYsLvsZ7XpMTbEIiQP5lB5u4IHjZQc2eevxfToGS2zw"  # A remplacer

culprit_information = requests.get(
    HINT_URL + "/" + culprit_playlist_id,
    headers={"Authorization": "Bearer {}".format(spotify_token)},
).content.decode()

culprit_name = json.loads(culprit_information)["owner"]["display_name"]

# Send culprit name to the police
CULPRIT_URL = "http://ripper.theo.do/api/culprit"
user_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxODQ0Mjg1LCJqdGkiOiI4NjRmY2ZjZjkxZGU0N2JkOTM4MjEwYzI2YWYwNWM4OCIsInVzZXJfaWQiOjIzM30.irR-H4MsqpKg-koOaU1kctRsQQzv7cZ8TYFbt-T-09M"  # A remplacer

police_answer = requests.post(
    CULPRIT_URL,
    data={"culprit_name": culprit_name},
    headers={"Authorization": "Bearer {}".format(user_token)},
).content.decode()

print(police_answer)

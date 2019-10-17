import requests

HINT_URL = "https://api.spotify.com/v1/playlists"

culprit_id = "2Ph7K8wOLOeJkcqLfhVSYu"

spotify_token = "BQAio4xleZ9KlQ5FXVZiVkefKDgioyiLMgrrrzrflye4aQ4jU6fI1NTj8ngt66pMcxGp5ECV2YeSBpwN4UwKUF9dFgx0VNhjk-x0f3i6oVdQm09gSEie-SBbMWrEsXs-6D9u44zGMvpex18WDGyEnS6k0QcilBgEjQ"  # A remplacer

culprit_information = requests.get(
    HINT_URL + "/" + culprit_id,
    headers={"Authorization": "Bearer {}".format(spotify_token)},
).content.decode()

print(culprit_information)

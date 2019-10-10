import json

# Renseigne les infos de l'énigme précédente
USERNAME = "myUserName"
ID = "123"

# Indique le nom du fichier contenant les coordonnées de tous les informateurs
FILE_NAME = "./addresses.json"

with open(FILE_NAME) as addresses_file:
    addresses = json.load(addresses_file)

    # Reconstruis la clé associée à ton username
    username_key = USERNAME + "-" + ID

    # Récupère les coordonnées de l'informateur
    address_to_visit = addresses[username_key]

    # Affiche les coordonnées de l'informateur
    print(address_to_visit)

import json

# Renseigne les infos de l'enigme precedente
USERNAME = "myUserName"
ID = "123"

# Indique le nom du fichier contenant les coordonnees de tous les informateurs
FILE_NAME = "./addresses.json"

with open(FILE_NAME) as addresses_file:
    addresses = json.load(addresses_file)

    # Reconstruis la cle associee a ton username
    username_key = USERNAME + "-" + ID

    # Recupere les coordonnees de l'informateur
    address_to_visit = addresses[username_key]

    # Affiche les coordonnees de l'informateur
    print(address_to_visit)

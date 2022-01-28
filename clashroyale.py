import requests, secrets

authkey = secrets.authkey

url = "https://api.clashroyale.com/v1/clans/%2328UCV9L0/currentriverrace"
head = {"Authorization": "Bearer {}".format(authkey)}

response = requests.get(url=url, headers=head).json()

for players in response["clan"]["participants"]:
    if players["decksUsedToday"] < 4:
        print("Tag:            " + players["tag"])
        print("Name:           " + players["name"])
        print("Decks übrig:    " + str(4 - (players["decksUsedToday"])))
        print("")

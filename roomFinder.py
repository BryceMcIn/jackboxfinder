import requests # Used for HTTP Requests
import string   # Used for list of uppercase
import random   # Used to generate random room codes

# chars = list of uppercase ascii chars
# base = url for jackbox room api
chars = string.ascii_uppercase
base = 'https://ecast.jackboxgames.com/api/v2/rooms/'

while(True):
    # Generate room code (4 random uppercase chars)
    roomCode = ''.join(random.choice(chars) for _ in range(4))
    url = base + roomCode

    # Query the API and parse response
    r = requests.get(url)
    jackboxResponse = r.json()

    #If a valid room code is found
    if(jackboxResponse["ok"] == True):
        print("\nHIT!!!! : " + roomCode + '\n')


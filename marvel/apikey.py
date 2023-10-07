import requests

ts = 1
private_key = "f201dfef12dc9c255ab0e94ffd95cd13a91ab455"
public_key = "5249ecc00549b55bbd7b13eb75bb86d1"
# 1f201dfef12dc9c255ab0e94ffd95cd13a91ab4555249ecc00549b55bbd7b13eb75bb86d1
hashed = "0dc062805f6d58a29bbeeabf1a365c55"
url = f"https://gateway.marvel.com:443/v1/public/characters?ts={ts}&apikey={public_key}&hash={hashed}"
print(url)

response = requests.get(url)
print(response)
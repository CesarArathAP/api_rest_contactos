import requests

URI = "http://localhost:8000/v1/contactos"
response = requests.get(URI)

print(f"GET : {response.text}")
print(f"GET : {response.status_code}")
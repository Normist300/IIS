import requests

resp2 = requests.get('http://127.0.0.1:8000/pets')
print(resp2.json())

# resp2 = requests.post('http://127.0.0.1:8000/pets', json={"id":"0", "name":"test"})
# print(resp2.json())
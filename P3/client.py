import requests

# re = requests.get('http://127.0.0.1:8000/pets')
# print(r.json())

r = requests.post('http://127.0.0.1:8000/books/', json={"title": "Пикник на обочине",
                                                        "author": "Братья Стругацкие",
                                                        "year": "1972"})
print(r.json())
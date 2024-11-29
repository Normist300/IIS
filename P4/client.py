import requests

# re = requests.get('http://127.0.0.1:8000/pets')
# print(r.json())

# r = requests.post('http://127.0.0.1:8000/book/', json={"title": "Книга",
#                                                         "author": "Автор",
#                                                         "year": "2000"})
# print(r.json())

# r = requests.get('http://127.0.0.1:8000/book/all')
# print(r.json())

# r = requests.put('http://127.0.0.1:8000/book/2', json={"title": "Война и мир",
#                                                         "author": "Лев Толстой",
#                                                         "year": "1863"})
# print(r.json())

r = requests.get('http://127.0.0.1:8000/book/2')
print(r.json())
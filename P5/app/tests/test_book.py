from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.models import Base
from app.db.session import get_db


def override_get_db():
    engine = create_engine("sqlite:///./library.db")
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_book():
    print ("создание")
    response = client.post("/books/",json={"title": "string", "author": "string", "id": 6})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "string"
    assert data["author"] == "string"
    assert data["id"] == 6

    # добавьте код проверяющий что читаль действительно создался с нужными параметрами

    book_id = 6
    # Получаем читателя
    response = client.get(f"/books/{book_id}/")
    print(response.status_code)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "string"
    assert data["author"] == "string"
    assert data["id"] == book_id

def test_get_book():
    print ("чтение")
    # response = client.post("/books/",json={"name": "string"})
    # assert response.status_code == 200
    # data = response.json()
    # assert data["name"] == "string"
    # assert data["id"] == 7
    # print(data["id"])

    book_id = 6
    # Получаем читателя
    response = client.get(f"/books/{book_id}/")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "string"
    assert data["author"] == "string"
    assert data["id"] == book_id

def test_delete_book():
    id = 6
    response = client.delete(f"/books/{id}/")
    assert response.status_code == 200

def test_all_books():
    response = client.get(f"/books/")
    assert response.status_code == 200
    assert len(response.json()) == 5

# test_create_book()
# test_get_book()
# test_delete_book()
# test_all_books()
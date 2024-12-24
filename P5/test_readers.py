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

def test_create_reader():
    print ("создание")
    response = client.post("/readers/",json={"name": "Марина"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Марина"
    assert data["id"] == 9

    # добавьте код проверяющий что читаль действительно создался с нужными параметрами

    reader_id = 9
    # Получаем читателя
    response = client.get(f"/readers/{reader_id}/")
    print(response.status_code)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == reader_id
    assert data["name"] == "Марина"

def test_get_reader():
    print ("чтение")
    # response = client.post("/readers/",json={"name": "string"})
    # assert response.status_code == 200
    # data = response.json()
    # assert data["name"] == "string"
    # assert data["id"] == 7
    # print(data["id"])

    reader_id = 7
    # Получаем читателя
    response = client.get(f"/readers/{reader_id}/")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == reader_id
    assert data["name"] == "string"

def test_delete_reader():
    id = 1
    response = client.delete(f"/readers/{id}/")

test_create_reader()
# test_get_reader()
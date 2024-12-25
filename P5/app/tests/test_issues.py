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

def test_create_issue():
    print ("создание")
    response = client.post("/issues/",json={"book_id": 3, "reader_id": 3, "id": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["reader_id"] == 3
    assert data["id"] == 3
    assert data["book_id"] == 3

    # добавьте код проверяющий что читаль действительно создался с нужными параметрами

    issue_id = 3
    # Получаем читателя
    response = client.get(f"/issues/{issue_id}/")
    print(response.status_code)
    assert response.status_code == 200
    data = response.json()
    assert data["reader_id"] == issue_id
    assert data["id"] == issue_id
    assert data["book_id"] == issue_id

def test_get_issue():
    print ("чтение")
    # response = client.post("/issues/",json={"name": "string"})
    # assert response.status_code == 200
    # data = response.json()
    # assert data["name"] == "string"
    # assert data["id"] == 7
    # print(data["id"])

    issue_id = 3
    # Получаем читателя
    response = client.get(f"/issues/{issue_id}/")
    assert response.status_code == 200
    data = response.json()
    assert data["reader_id"] == issue_id
    assert data["id"] == issue_id
    assert data["book_id"] == issue_id

def test_delete_issue():
    id = 3
    response = client.delete(f"/issues/{id}/")
    assert response.status_code == 200

def test_all_issues():
    response = client.get(f"/issues/")
    assert response.status_code == 200
    assert len(response.json()) == 2

# test_create_issue()
# test_get_issue()
# test_delete_issue()
# test_all_issues()
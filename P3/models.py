from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book(BaseModel):
    title: str = Field(..., title="Название книги", max_length=100)
    author: str = Field(..., title="Имя автора", max_length=50)
    year: int = Field(..., title="Год издания", ge=1450, le=2024)

@app.post("/books/")
def create_book(book: Book):
    return {"message": f"Книга '{book.title}' добавлена!", "data": book}
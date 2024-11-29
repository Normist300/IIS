from fastapi import APIRouter, HTTPException
from app.models import Book
from app.database import get_all_books, get_book, add_book, update_book, delete_book

rt = APIRouter()

@rt.get("/book/all", response_model=list[Book])
async def read_books():
    """Получить список всех книг."""
    return get_all_books()

@rt.get("/book/{book_id}", response_model=Book)
async def read_book(book_id: int):
    """Получить книгу по ID."""
    book = get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@rt.post("/book", response_model=Book)
async def create_book(book: Book):
    """Добавить новую книги."""
    book_data = book.model_dump()
    book_id = add_book(book_data)
    return get_book(book_id)

@rt.put("/book/{book_id}", response_model=Book)
async def update_book_info(book_id: int, book: Book):
    """обновить информацию о книге."""
    existing_book = get_book(book_id)
    if existing_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    updated_book = update_book(book_id, book.model_dump(exclude_unset=True))
    return updated_book

@rt.delete("/book/{book_id}")
async def delete_book_info(book_id: int):
    """Удалить книгу по ID."""
    if get_book(book_id) is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    delete_book(book_id)
    return {"message": "Книга успешно удалена"}
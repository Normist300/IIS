from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    year: int

# Идентификатор книги
# Название книги
# Автор книги
# Год издания книги
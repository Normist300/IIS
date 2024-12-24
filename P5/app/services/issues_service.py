from sqlalchemy.orm import Session
from app.db.models import Issue, Book, Reader
from app.models.issue import IssueCreate

class IssueService:
    @staticmethod
    def create_issue(db: Session, issue_data: IssueCreate) :
        '''
        Создаёт новую выдачу книги читателю
        '''
        # Проверка, что книга существует и не выдана
        book = db.query(Book).filter(Book.id == issue_data.book_id).first()
        if not book:
            raise ValueError(f"Книга с ID {issue_data.book_id} не найдена")
        
        existing_issue = db.query(Issue).filter(Issue.book_id == issue_data.book_id).first()
        if existing_issue:
            raise ValueError(f"Книга с ID {issue_data.book_id} уже выдана")
        
        # Проверка, что читатель существует
        reader = db.query(Reader).filter(Reader.id == issue_data.reader_id).first()
        if not reader:
            raise ValueError(f"Читатель с ID {issue_data.reader_id} не найден")
        
        # Создание новой выдачи
        issue = Issue( ** issue_data.model_dump() )
        db.add(issue)
        db.commit()
        db.refresh(issue)
        return issue
    
    
    @staticmethod
    def get_issue(db: Session, issue_id: int):
        '''
        Получает информацию о выдаче по её ID.
        '''
        issue = db.query(Issue).filter(Issue.id == issue_id).first()
        if not issue:
            raise ValueError(f"Выдача c ID {issue_id} не найдена")
        return issue
    
    @staticmethod
    def get_all_issues(db: Session):
        issues = db.query(Issue).all()
        if not issues:
            raise ValueError(f'Error by fetching issues')
        '''
        Возращает список всех выдач.
        '''
        return issues
    
    @staticmethod
    def close_issue(db: Session, issue_id: int):
        '''
        Закрывает выдачу, удаляя запись о ней (возрат книги).
        '''
        issue = db.query(Issue).filter(Issue.id == issue_id).first()
        if not issue:
            raise ValueError(f"Выдача c ID {issue_id} не найдена")
        
        db.delete(issue)
        db.commit()
        return {"message": f"Выдача c ID {issue_id} зыкрыта"}
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Create the FastAPI app
app = FastAPI(title="Library Book Management API")

# Optional home route
@app.get("/")
def home():
    return {"message": "Welcome to the Book API! Visit /docs to explore the endpoints."}

# Database setup
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# SQLAlchemy model for Book
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String, nullable=True)

# Create the database table
Base.metadata.create_all(bind=engine)

# Pydantic models for request and response
class BookCreate(BaseModel):
    title: str
    author: str
    description: str | None = None

class BookResponse(BookCreate):
    id: int

    model_config = {
        "from_attributes": True
    }

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new book
@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Get all books
@app.get("/books", response_model=list[BookResponse])
def read_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

# Get a specific book by ID
@app.get("/books/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Update a book by ID
@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated_book: BookCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = updated_book.title
    book.author = updated_book.author
    book.description = updated_book.description
    db.commit()
    db.refresh(book)
    return book

# Delete a book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": f"Book with ID {book_id} deleted successfully"}

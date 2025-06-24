# -  Create a dataclass to represent a library book with fields for title, author, ISBN, and publication year,
#  including a method to display book details
from dataclasses import dataclass
from typing import Optional
from datetime import date
@dataclass
class Book:
    title: str  
    author: str
    isbn: str
    publication_year: Optional[int] = None
    publication_date: Optional[date] = None
    def display_details(self):
        details = f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"
        if self.publication_year:
            details += f"\nPublication Year: {self.publication_year}"
        if self.publication_date:
            details += f"\nPublication Date: {self.publication_date.strftime('%Y-%m-%d')}"
        return details  
if __name__ == "__main__": 
    book1 = Book(title="1984", author="George Orwell", isbn="1234567890", publication_year=1949)
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="0987654321", publication_date=date(1960, 7, 11))
    
    print(book1.display_details())
    print(book2.display_details())

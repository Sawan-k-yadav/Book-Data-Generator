# Import the database instance from the database.py file
from app.database import db

# Define the Book model
class Book(db.Model):
    """
    Represents a book in the database.
    
    Attributes:
    id (int): The unique identifier for the book.
    title (str): The title of the book.
    author (str): The author of the book.
    genre (str): The genre of the book.
    language (str): The language of the book.
    subject (str): The subject of the book.
    bookshelf (str): The bookshelf where the book belongs.
    links (list): A list of links to download the book in different formats.
    """
    
    # Define the columns for the Book table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the book
    title = db.Column(db.String(200), nullable=False)  # Title of the book
    author = db.Column(db.String(100), nullable=False)  # Author of the book
    genre = db.Column(db.String(50), nullable=False)  # Genre of the book
    language = db.Column(db.String(20), nullable=False)  # Language of the book
    subject = db.Column(db.String(100), nullable=False)  # Subject of the book
    bookshelf = db.Column(db.String(100), nullable=False)  # Bookshelf where the book belongs
    
    # Define the relationship between the Book model and the Link model
    links = db.relationship('Link', backref='book', lazy=True)

# Define the Link model
class Link(db.Model):
    """
    Represents a link to download a book in a specific format.
    
    Attributes:
    id (int): The unique identifier for the link.
    book_id (int): The identifier of the book that the link belongs to.
    mime_type (str): The MIME type of the link.
    link (str): The URL of the link.
    """
    
    # Define the columns for the Link table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the link
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)  # Identifier of the book that the link belongs to
    mime_type = db.Column(db.String(20), nullable=False)  # MIME type of the link
    link = db.Column(db.String(200), nullable=False)  # URL of the link
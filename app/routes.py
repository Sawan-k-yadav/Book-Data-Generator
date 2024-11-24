# Import the Flask app instance and the Book model
from app import app
from flask import Flask, render_template, request
from app.models import Book, Link

# Define the route for the homepage
@app.route('/')
def index():
    """
    Displays the homepage with a list of all books.
    
    Returns:
    A rendered HTML template with a list of books.
    """
    
    # Query the database for all books
    books = Book.query.all()
    
    # Render the HTML template with the list of books
    return render_template('index.html', books=books)

# Define the route for displaying a single book's details
@app.route('/book/<int:book_id>')
def book_details(book_id):
    """
    Displays the details of a single book.
    
    Args:
    book_id (int): The ID of the book to display.
    
    Returns:
    A rendered HTML template with the book's details.
    """
    
    # Query the database for the book with the specified ID
    book = Book.query.get(book_id)
    
    # If the book is not found, return a 404 error
    if book is None:
        return render_template('404.html'), 404
    
    # Render the HTML template with the book's details
    return render_template('book_details.html', book=book)

# Define the route for searching books
@app.route('/search')
def search_books():
    """
    Searches for books based on the query parameter.
    
    Returns:
    A rendered HTML template with the search results.
    """
    
    # Get the query parameter from the URL
    query = request.args.get('query')
    
    # Query the database for books that match the search query
    books = Book.query.filter(Book.title.like('%' + query + '%')).all()
    
    # Render the HTML template with the search results
    return render_template('search_results.html', books=books)

# def main():
#     app.run()
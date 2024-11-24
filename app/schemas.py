# Import the Marshmallow library
from marshmallow import Schema, fields

# Define the BookSchema
class BookSchema(Schema):
    """
    A schema for serializing and deserializing Book objects.
    """
    
    # Define the fields for the Book schema
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    genre = fields.Str(required=True)
    language = fields.Str(required=True)
    subject = fields.Str(required=True)
    bookshelf = fields.Str(required=True)
    links = fields.Nested('LinkSchema', many=True)

# Define the LinkSchema
class LinkSchema(Schema):
    """
    A schema for serializing and deserializing Link objects.
    """
    
    # Define the fields for the Link schema
    id = fields.Int(dump_only=True)
    book_id = fields.Int(required=True)
    mime_type = fields.Str(required=True)
    link = fields.Str(required=True)
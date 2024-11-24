from flask import Flask, render_template, request
from app.config import Config
from app.database import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Create all tables
with app.app_context():
    db.create_all()

from app.routes import app

# if __name__ == '__main__':
#     app.run()
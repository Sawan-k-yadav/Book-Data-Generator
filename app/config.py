import os
from sqlalchemy import create_engine

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:sawan@localhost:3306/gutendex'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = 'secret_key_here'
    # TEMPLATE_FOLDER = 'templates'
    # STATIC_FOLDER = 'static'
    # engine.execute('CREATE DATABASE IF NOT EXISTS gutendex;')
    # engine.execute('USE gutendex;')


import os
from pathlib import Path  #This Path library is used to handle any kind of path issue in any operating system
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [ 
    f"app/__init__.py",
    f"app/config.py",
    f"app/database.py",
    f"app/models.py",
    f"app/routes.py",
    f"app/schemas.py",
    f"app/templates/base.html",
    f"app/templates/book_details.html",
    f"app/templates/index.html",
    f"app/static/style.css",
    "requirements.txt",
    "README.md",
    ".gitignore"
    "setup.py"                     # This setup.py used for creating local package
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # Here we are checking this file path does not exist or if there is no data in that file then create 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass   # Creating an empty file here only
            logging.info(f"Creating Empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")


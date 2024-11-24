# Book Data Generation for Gutenberg database

### Steps to run the project

1. Clone the github repo in of your folder on local --
```
    git clone https://github.com/Sawan-k-yadav/Book-Data-Generator.git
```

2. Create virtual environment using conda or python --
``` 
    conda create -p dbgen python==3.7 -y
```
3. Activate virtual environment --
```
    conda activate dbgen/
    or
    source activate dbgen/
```
4. Install the required labraries --
```
    pip install -r requirements.txt
```
5. Run the program (make sure you database and table are created already)--
```
    python -m app
```
``` Here I am using -m for module which 'app' because I have created my app run logic inside __init__.py ```
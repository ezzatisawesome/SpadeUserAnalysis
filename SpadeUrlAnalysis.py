import os
from dotenv import load_dotenv
from pathlib import Path
from pymongo import MongoClient

dotenv_path = Path('./app.env')
load_dotenv(dotenv_path=dotenv_path)
API_KEY = os.getenv('API_KEY')
OUTLIER_USERS = os.getenv('OUTLIER_USERS')

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    sketches = db.sketches
    sketchesData = list(filter(lambda i: i['user_id'] not in OUTLIER_USERS , sketches.find()))

    

if __name__ == '__main__':
    main()

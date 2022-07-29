from dotenv import load_dotenv
import os
import json
from pathlib import Path
from pymongo import MongoClient
import random
import requests

dotenv_path = Path('./app.env')
load_dotenv(dotenv_path=dotenv_path)
API_KEY = os.getenv('API_KEY')
OUTLIER_USERS = os.getenv('OUTLIER_USERS')

def main():
    links = getLinks()
    sampledLinks = random.sample(links, 98)
    linkData = []
    for link in sampledLinks:
        linkData.append(classify(link))
    writeToFile(linkData)

def classify(link: str):
    url = "https://www.klazify.com/api/categorize"
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': "Bearer {key}".format(key=API_KEY),
        'cache-control': "no-cache"
    }
    payload = json.dumps({'url': bytes.fromhex(link).decode('utf-8')})
    response = requests.request("POST", url, data=payload, headers=headers)
    return json.loads(response.text)

def getLinks():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    sketchesData = db.sketches
    sketches = list(filter(lambda i: i['user_id'] not in OUTLIER_USERS, sketchesData.find()))
    linksArray = []
    for sketch in sketches:
        for i in range(len(sketch)):
            if i > 1:
                linksArray.append(list(sketch)[i])
    return linksArray

def writeToFile(data: list):
    with open("classificationData.json", "w") as outfile:
        outfile.write(json.dumps(data))

if __name__ == '__main__':
    main()

import os, requests
from dotenv import load_dotenv

load_dotenv()

TRELLO_KEY = os.getenv("TRELLO_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")

url = "https://api.trello.com/1/boards/"

query = {
    'key': TRELLO_KEY,
    'token': TRELLO_TOKEN,
    'name': 'Hackathon Test Board'
}

response = requests.post(url, params=query)

print("Status:", response.status_code)
print("Response:", response.json())
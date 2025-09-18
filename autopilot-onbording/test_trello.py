import os, requests
from dotenv import load_dotenv

load_dotenv()

TRELLO_KEY = os.getenv("TRELLO_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")

url = f"https://api.trello.com/1/members/me/boards?key={TRELLO_KEY}&token={TRELLO_TOKEN}"

response = requests.get(url)

print("Status:", response.status_code)
print("Response:", response.json())
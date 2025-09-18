import os, requests
from dotenv import load_dotenv

load_dotenv()

TRELLO_KEY = os.getenv("TRELLO_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")

def create_trello_board(project_name, project_goal):
    url = "https://api.trello.com/1/boards/"
    query = {
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN,
        'name': project_name,
        'desc': f"Project Goal: {project_goal}"
    }
    response = requests.post(url, params=query)
    if response.status_code == 200:
        board = response.json()
        print("✅ Trello Board Created:", board["url"])
        
        # Create default lists
        create_lists(board["id"])
        return board
    else:
        print("❌ Failed to create board:", response.text)
        return None


def create_lists(board_id):
    lists = ["To Do", "In Progress", "Done"]
    for list_name in lists:
        url = f"https://api.trello.com/1/lists"
        query = {
            'key': TRELLO_KEY,
            'token': TRELLO_TOKEN,
            'name': list_name,
            'idBoard': board_id
        }
        response = requests.post(url, params=query)
        if response.status_code == 200:
            print(f"✅ List created: {list_name}")
        else:
            print(f"❌ Failed to create list {list_name}: {response.text}")

def create_card(list_id, card_name, card_desc=""):
    url = "https://api.trello.com/1/cards"
    query = {
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN,
        'idList': list_id,
        'name': card_name,
        'desc': card_desc
    }
    response = requests.post(url, params=query)
    if response.status_code == 200:
        card = response.json()
        print(f"✅ Card created: {card_name} -> {card['shortUrl']}")
    else:
        print(f"❌ Failed to create card {card_name}: {response.text}")
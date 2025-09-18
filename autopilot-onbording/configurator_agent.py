# configurator_agent.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TRELLO_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")
BASE_URL = "https://api.trello.com/1"

def create_trello_board(board_name):
    url = f"{BASE_URL}/boards/"
    query = {
        'name': board_name,
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.post(url, params=query)
    return response.json()

def add_list(board_id, list_name):
    url = f"{BASE_URL}/boards/{board_id}/lists"
    query = {
        'name': list_name,
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.post(url, params=query)
    return response.json()

if __name__ == "__main__":
    board = create_trello_board("Marketing Campaign 2025")
    print("Board Created:", board["id"])
    add_list(board["id"], "To Do")
    add_list(board["id"], "In Progress")
    add_list(board["id"], "Done")
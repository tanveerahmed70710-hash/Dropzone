from flask import Flask, request, render_template, redirect, url_for
from configurator import create_trello_board, create_card
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_board_lists(board_id):
    TRELLO_KEY = os.getenv("TRELLO_KEY")
    TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
    url = f"https://api.trello.com/1/boards/{board_id}/lists?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
    return requests.get(url).json()

@app.route("/", methods=["GET", "POST"])
def home():
    status = []
    board_url = None
    board_name = None
    board_goal = None
    if request.method == "POST":
        project_name = request.form.get("project_name")
        project_goal = request.form.get("project_goal")
        status.append("📝 Interviewer: Collected project details.")
        board = create_trello_board(project_name, project_goal)
        if board:
            board_url = board.get("url")
            board_name = board.get("name")
            board_goal = project_goal
            status.append("📋 Configurator: Trello board created.")
            lists = get_board_lists(board["id"])
            todo_list = next((lst for lst in lists if lst["name"] == "To Do"), None)
            if todo_list:
                status.append("✅ Lists added: To Do, In Progress, Done.")
                # Add sample tasks
                create_card(todo_list["id"], "Define project scope", "Discuss with the team")
                create_card(todo_list["id"], "Set up integrations", "Connect with existing tools")
                create_card(todo_list["id"], "First review", "Prepare a demo for stakeholders")
                status.append("🗂️ Sample tasks added to 'To Do'.")
            else:
                status.append("⚠️ Could not find 'To Do' list.")
        else:
            status.append("❌ Failed to create Trello board.")
        return render_template("index.html", status=status, board_url=board_url, board_name=board_name, board_goal=board_goal)
    return render_template("index.html", status=None)

if __name__ == "__main__":
    app.run(debug=True)
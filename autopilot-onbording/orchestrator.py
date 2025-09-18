# orchestrator.py
from interviewer_agent import interviewer_agent
from configurator_agent import create_trello_board, add_list

def run_onboarding(user_input):
    # Step 1: Interviewer collects needs
    requirements = interviewer_agent(user_input)
    print("Requirements:", requirements)

    # Step 2: Configurator sets up Trello
    board = create_trello_board(requirements["goal"])
    print("Created Board:", board["name"])

    # Step 3: Add default lists
    for lst in ["To Do", "In Progress", "Done"]:
        add_list(board["id"], lst)

    return f"Board '{requirements['goal']}' created with lists!"

if __name__ == "__main__":
    result = run_onboarding("I want to manage a marketing campaign")
    print(result)
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def interviewer_agent(user_input):
    """
    Takes user input and extracts requirements.
    For hackathon, keep it simple.
    """
    # Dummy structured output (later: use GPT)
    if "marketing" in user_input.lower():
        goal = "Marketing Campaign"
    else:
        goal = "General Project"

    return {
        "goal": goal,
        "team_size": 5,  # could ask follow-up
        "integration": "Google Drive"
    }

if __name__ == "__main__":
    user_text = "I want to manage a marketing campaign with my 5-person team"
    print(interviewer_agent(user_text))
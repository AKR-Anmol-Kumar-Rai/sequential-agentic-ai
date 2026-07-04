from agno.agent import Agent
from agno.models.groq.groq import Groq
from tools.execute_tools import run_code

from dotenv import load_dotenv
load_dotenv()

debugging_agent = Agent(
    model=Groq(
        id="llama-3.3-70b-versatile",
        max_tokens=500
    ),
    description="Analyze Python errors and fix code",
    instructions=[
        "You will receive Python code and an error message.",
        "Analyze both carefully.",
        "Fix the code based on the error.",
        "Return ONLY corrected raw Python code.",
        "Do not explain anything.",
        "Do not use markdown.",
        "Do not add ```python blocks."
    ]
)
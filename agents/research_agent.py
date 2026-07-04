from agno.agent import Agent
from agno.models.groq.groq import Groq
from dotenv import load_dotenv
load_dotenv()

research_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile",max_tokens=500),
    description="Research best methods for solving user problem",
    instructions=[
        "Analyze the user query",
        "Identify problem type",
        "Suggest algorithms",
        "Suggest preprocessing steps",
        "Suggest evaluation metrics"
    ]
)
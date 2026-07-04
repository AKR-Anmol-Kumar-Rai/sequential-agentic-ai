from agno.agent import Agent
from agno.models.groq.groq import Groq
from dotenv import load_dotenv
load_dotenv()


planning_agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile",max_tokens=500),
    description="Create step by step plan for coding"
)
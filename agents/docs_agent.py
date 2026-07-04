from agno.agent import Agent
from agno.models.groq.groq import Groq
from tools.file_tools import create_downloadable_file

from dotenv import load_dotenv
load_dotenv()

docs_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile",max_tokens=500),
    description="Generate README",
    tools=[create_downloadable_file]
)
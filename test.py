from agno.agent import Agent
from agno.models.ollama import Ollama
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model = Ollama(id="qwen2.5:7b"),
    description="you are a news reporter and sescriep every detailed news"
)
agent.print_response("tell me situation in iraq")
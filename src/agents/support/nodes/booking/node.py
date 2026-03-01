from langchain.agents import create_agent

from .tools import tools
from .prompt import prompt_template

booking_node = create_agent(
    model="openai:gpt-4o-mini",
    tools=tools,
    system_prompt=prompt_template.format(),
)

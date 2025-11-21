from agents.support.nodes.conversation.prompt import SYSTEM_PROMPT
from agents.support.nodes.conversation.tools import TOOLS
from agents.support.state import State

from langchain.chat_models import init_chat_model

llm = init_chat_model(model="openai:gpt-4o-mini", temperature=1)
llm = llm.bind_tools(TOOLS)

def conversation(state: State):
    new_state: State = {}
    history = state.get("messages", [])
    last_message = history[-1]
    customer_name = state.get("customer_name", "John Doe")
    # system_message = f"You are a helpful assistant that can answer questions about the customer {customer_name}"
    ai_message = llm.invoke([("system", SYSTEM_PROMPT), ("user", last_message.text)])
    new_state["messages"] = [ai_message]
    return new_state
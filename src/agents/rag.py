import random
from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage
from langchain.chat_models import init_chat_model

llm = init_chat_model(model="openai:gpt-4o", temperature=1)
file_search_tool = {
    "type": "file_search",
    "vector_store_ids": ["vs_691b86cb24788191ad17cfdc400f3e4a"],
}
llm = llm.bind_tools([file_search_tool])

class State(MessagesState):
    customer_name: str
    my_age: int

def node_1(state: State):
    new_state: State = {}
    if state.get("customer_name", None) is None:
        new_state["customer_name"] = "John Doe"
    else:
        new_state["my_age"] = random.randint(18, 65)
    
    history = state.get("messages", [])
    last_message = history[-1]
    ai_message = llm.invoke(last_message.text)
    new_state["messages"] = [ai_message]
    print(new_state)
    return new_state

from langgraph.graph import END, StateGraph, START

builder = StateGraph(State)
builder.add_node("node_1", node_1)

builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

agent = builder.compile()


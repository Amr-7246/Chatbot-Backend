import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

# * Load .env
load_dotenv()

def create_agent():
    # ~ Give a Memory for Our Agent
    memory = MemorySaver()

    # ~ Define our LLM
    model = ChatAnthropic(
        model_name="claude-3-sonnet-20240229",
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )

    # ~ Select our Tools to give it to our LLM
    search = TavilySearchResults(
        api_key=os.getenv("TAVILY_API_KEY"), 
        max_results=2
        )
    tools = [search]

    # ~ invok the Agent
    agent_executor = create_react_agent(model, tools, checkpointer=memory)
    
    # ~ Return a wrapped function for CLI or server use (to consume the agent)
    class AgentWrapper:
        def run(self, prompt: str):
            config = {"configurable": {"thread_id": "abc123"}}
            result = ""
            for step in agent_executor.stream(
                {"messages": [{"type": "human", "content": prompt}]},
                config,
                stream_mode="values",
            ):
                msg = step["messages"][-1]
                result += msg.content + "\n"
            return result.strip()
    return AgentWrapper()
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI


# Define your LLM with timeout
llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo",
    timeout=60  # 60 seconds timeout
)

# Define your Agent
researcher = Agent(
    role="SEO Researcher",
    goal="Find trending and high-ranking SEO keywords for a given topic",
    backstory="You are an expert at discovering SEO trends and valuable keywords that can rank on Google.",
    tools=[SerperDevTool()],
    verbose=True,
    llm=llm  # Injecting custom LLM with timeout
)

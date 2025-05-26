from crewai import Agent
from langchain_openai import ChatOpenAI


# Configure the LLM with timeout
llm = ChatOpenAI(temperature=0.7, timeout=60)  # 60 seconds timeout

# Define the SEO Writer agent
seo_writer = Agent(
    role="SEO Writer",
    goal="Write engaging and SEO-optimized blog content",
    backstory=(
        "A professional content writer with years of experience in crafting high-ranking SEO blog posts. "
        "You know how to structure content, use keywords effectively, and keep readers engaged."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm  # 👈 Inject the customized LLM with timeout
)

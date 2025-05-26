from crewai import Task
from tools.serper_tool import SerperTool

def keyword_research_task(agent):
    return Task(
        description="Research trending and high-ranking SEO keywords for the given topic.",
        expected_output="A list of top SEO keywords with volume and ranking difficulty.",
        agent=agent,
        tools=[SerperTool()]
    )

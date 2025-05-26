from crewai import Crew
from Agents.researcher import researcher
from Agents.seo_writer import seo_writer
from Tasks.keyword_research import keyword_research_task
from Tasks.write_blog import write_blog_task



def create_seo_crew():
    # Define the tasks using your agents
    tasks = [
        keyword_research_task(researcher),
        write_blog_task(seo_writer)
    ]

    # Assemble the Crew
    crew = Crew(
        agents=[researcher, seo_writer],
        tasks=tasks,
        verbose=True
    )

    return crew

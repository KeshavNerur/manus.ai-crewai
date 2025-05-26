from crewai import Task

def write_blog_task(agent):
    return Task(
        description="Write a 500-word blog post using the researched keywords. Ensure SEO best practices.",
        expected_output="An engaging and well-structured SEO-optimized blog post.",
        agent=agent
    )

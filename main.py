from dotenv import load_dotenv
import sys
import os

# Load environment variables
load_dotenv()

# ✅ Print API keys to check if they're loaded
print("OpenAI Key:", os.getenv("OPENAI_API_KEY"))
print("Serper Key:", os.getenv("SERPER_API_KEY"))

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crews.seo_blog_crew import create_seo_crew

if __name__ == "__main__":
    crew = create_seo_crew()
    result = crew.kickoff()

    with open("outputs/blogs/generated_blog.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("\n✅ Blog post saved to outputs/blogs/generated_blog.txt")



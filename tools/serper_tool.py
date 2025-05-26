import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# Load .env variables
load_dotenv()

# Optionally check if key is present
serper_api_key = os.getenv("SERPER_API_KEY")
if not serper_api_key:
    raise ValueError("SERPER_API_KEY not found in .env file!")

# Instantiate the tool
def SerperTool():
    return SerperDevTool()


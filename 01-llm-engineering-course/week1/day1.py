"""
Day 1: LLM Engineering Course
"""

# Import libraries
# - os: for environment variables
import os
# - dotenv: for loading environment variables
from dotenv import load_dotenv
# - openai: for interacting with the OpenAI API
from openai import OpenAI
# - scraper: for fetching website content
from scraper import fetch_website_contents
# - IPython.display: for displaying Markdown in Jupyter notebooks
from IPython.display import Markdown, display


# Load environment variables
load_dotenv(override=True)

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded
if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")
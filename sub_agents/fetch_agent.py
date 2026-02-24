from google.adk import Agent
from tools.github_tools import fetch_github_repos
fetch_agent = Agent(
    name="FetchAgent",
    tools=[fetch_github_repos],
)

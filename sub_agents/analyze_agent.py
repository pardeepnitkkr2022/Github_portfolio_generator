from google.adk import Agent
from tools.analysis_tools import analyze_repositories
analyze_agent = Agent(
    name="AnalyzeAgent",
    tools=[analyze_repositories],
)

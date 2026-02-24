from google.adk import Agent
from sub_agents.fetch_agent import fetch_agent
from sub_agents.analyze_agent import analyze_agent
from sub_agents.report_agent import report_agent
root_agent = Agent(
    name="RootAgent",
    sub_agents=[
        fetch_agent,
        analyze_agent,
        report_agent
    ],
)

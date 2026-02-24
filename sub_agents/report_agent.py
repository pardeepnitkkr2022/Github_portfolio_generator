from google.adk import Agent
from tools.report_tools import generate_markdown_report
report_agent = Agent(
    name="ReportAgent",
    tools=[generate_markdown_report],
)

# GitHub Portfolio Generator (Google ADK)

This application is developed using the Google Agent Development Kit (ADK) and follows a multi-agent architecture. It automatically creates a structured GitHub portfolio overview for any public GitHub user by collecting and processing repository data.

## Architecture

RootAgent – Acts as the central coordinator and manages the overall execution flow.

FetchAgent – Connects to the GitHub API and retrieves public repository information for the specified user.

AnalyzeAgent – Examines repository data to determine primary languages, star count, and overall popularity.

ReportAgent – Converts the analyzed information into a well-formatted Markdown portfolio summary.

## Tools Used

- GitHub API integration module  
- Repository data analysis component  
- Markdown report generation utility  

## How to Run

```bash
python -m google.adk.cli run .
```

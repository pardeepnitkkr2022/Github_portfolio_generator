# GitHub Portfolio Generator using Google ADK

A multi-agent system built with the Google Agent Development Kit (ADK) that automatically generates a structured GitHub portfolio summary for any public GitHub username.

The application retrieves repository data, analyzes key metrics, and produces a clean Markdown portfolio report.

---

## Project Overview

This project follows a modular multi-agent architecture. Each agent has a clearly defined responsibility, making the system organized, scalable, and easy to extend.

Given a public GitHub username, the system:

- Fetches repository data
- Analyzes languages and popularity metrics
- Generates a formatted portfolio summary

---

## Architecture

### RootAgent
The central coordinator of the system.  
It manages the execution flow and ensures communication between all agents.

### FetchAgent
Responsible for interacting with the GitHub REST API to retrieve public repository information.

### AnalyzeAgent
Processes repository data to extract:

- Programming languages used
- Most popular repositories (based on stars/forks)
- Repository activity insights

### ReportAgent
Formats the analyzed data and generates a well-structured Markdown portfolio summary.

---

## Tools Used

- Custom GitHub API integration tool  
- Repository analysis utility  
- Markdown report generator  

---

## Workflow

1. The user provides a GitHub username.
2. FetchAgent retrieves all public repositories.
3. AnalyzeAgent evaluates repository statistics.
4. ReportAgent generates the final markdown portfolio.
5. RootAgent orchestrates the complete workflow.

---

## Installation

Ensure Python is installed and required dependencies are configured.

---

## How to Run

```bash
python -m google.adk.cli run .
```

---

## Output

The system generates a Markdown-based GitHub portfolio summary containing:

- GitHub profile overview  
- Repository highlights  
- Language distribution  
- Popular projects  

---

## Extensibility

The modular agent-based design allows easy integration of:

- Additional analytics
- Advanced ranking algorithms
- Visual portfolio enhancements
- Export formats beyond Markdown
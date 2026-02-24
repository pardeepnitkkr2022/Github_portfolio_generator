import requests
from typing import List, Dict, Any
def fetch_github_repos(username: str) -> List[Dict[str, Any]]:
    """Fetch public GitHub repositories"""
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

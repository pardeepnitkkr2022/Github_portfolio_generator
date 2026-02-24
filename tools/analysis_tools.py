from typing import List, Dict, Any
def analyze_repositories(repos: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze repositories for languages and stars"""
    languages: Dict[str, int] = {}
    top_repo = None
    max_stars = -1
    for repo in repos:
        lang = repo.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
        stars = repo.get("stargazers_count", 0)
        if stars > max_stars:
            max_stars = stars
            top_repo = repo.get("name")
    return {
        "languages": languages,
        "top_repo": top_repo
    }

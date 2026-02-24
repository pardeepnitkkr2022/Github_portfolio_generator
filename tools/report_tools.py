from typing import Dict, Any
def generate_markdown_report(username: str, analysis: Dict[str, Any]) -> str:
    """Generate markdown portfolio"""
    md = f"# GitHub Portfolio: {username}\n\n"
    md += "## Top Repository\n"
    md += f"- **{analysis.get('top_repo')}**\n\n"
    md += "## Languages Used\n"
    for lang, count in analysis.get("languages", {}).items():
        md += f"- {lang}: {count} repositories\n"
    return md

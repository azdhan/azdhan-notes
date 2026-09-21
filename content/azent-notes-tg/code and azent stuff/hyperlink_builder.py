import urllib.parse
from datetime import datetime

def build_search_urls(question: str) -> dict:
    q = urllib.parse.quote(question)
    return {
        "Google": f"https://www.google.com/search?q={q}",
        "ChatGPT": f"https://chat.openai.com/?q={q}",
        "Claude": f"https://claude.ai/search?q={q}",
        "DuckAI": f"https://duckduckgo.com/?q={q}",
    }

def date_line() -> str:
    return f"(Agent noted on {datetime.now().strftime('%Y-%m-%d')})"

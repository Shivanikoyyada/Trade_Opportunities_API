import requests


def collect_data(sector: str):

    query = f"India {sector} market news"

    url = f"https://api.duckduckgo.com/?q={query}&format=json"

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return ["Unable to fetch market news"]

    data = response.json()

    results = []

    for topic in data.get("RelatedTopics", [])[:5]:
        if "Text" in topic:
            results.append(topic["Text"])

    if not results:
        results.append("Limited news data available")

    return results
from datetime import datetime


def build_markdown(sector: str, analysis: str):

    report = f"""
# Trade Opportunity Report

**Sector:** {sector}

**Generated On:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

## AI Market Analysis

{analysis}

---

## Disclaimer

This report is AI-generated and should not be considered financial advice.
"""

    return report
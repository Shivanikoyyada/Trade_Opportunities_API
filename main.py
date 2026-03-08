from fastapi import FastAPI, Depends, HTTPException, Request
from services.data_collector import collect_data
from services.ai_analyzer import analyze_data
from utils.markdown_builder import build_markdown
from security.auth import verify_token
from security.rate_limiter import limiter
from config import VALID_SECTORS, RATE_LIMIT

app = FastAPI(
    title="Trade Opportunities API",
    description="AI-powered sector analysis for Indian markets",
    version="1.0"
)

@app.get("/analyze/{sector}")
@limiter.limit(RATE_LIMIT)
async def analyze_sector(request: Request, sector: str, user=Depends(verify_token)):

    sector = sector.lower()

    if sector not in VALID_SECTORS:
        raise HTTPException(
            status_code=400,
            detail=f"Sector not supported. Available sectors: {VALID_SECTORS}"
        )

    try:
        news_data = collect_data(sector)

        analysis = analyze_data(sector, news_data)

        report = build_markdown(sector, analysis)

        return {
            "sector": sector,
            "report": report
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
# Trade Opportunities API

## Overview

Trade Opportunities API is a FastAPI-based backend service that analyzes market data and generates trade opportunity insights for different sectors in India.

The system collects recent market information, analyzes it using an AI model, and returns a structured markdown report.

## Features

* Sector-based market analysis
* AI-powered insights using Gemini API
* Data collection from web sources
* Structured markdown report generation
* Rate limiting for abuse prevention
* Authentication for API access
* Input validation and error handling

## Tech Stack

* FastAPI
* Python
* Google Gemini API
* Uvicorn
* SlowAPI (rate limiting)

## API Endpoint

### Analyze Sector

GET /analyze/{sector}

Example:

GET /analyze/technology

### Sample Response

```json
{
  "sector": "technology",
  "report": "# Trade Opportunity Report\n\nMarket Overview..."
}
```

## Supported Sectors

* technology
* pharmaceuticals
* agriculture
* banking
* energy

## Project Structure

```
project/
│
├── main.py
├── config.py
│
├── services/
│   ├── data_collector.py
│   └── ai_analyzer.py
│
├── security/
│   ├── auth.py
│   └── rate_limiter.py
│
├── utils/
│   └── markdown_builder.py
```

## Installation

1. Clone the repository

```
git clone https://github.com/Shivanikoyyada/Trade-Opportunities-API.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the server

```
uvicorn main:app --reload
```

## API Documentation

Interactive documentation is available at:

```
http://127.0.0.1:8000/docs
```

## Security Features

* Token-based authentication
* Rate limiting per user/session
* Input validation

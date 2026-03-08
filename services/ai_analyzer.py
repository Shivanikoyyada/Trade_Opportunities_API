# import google.generativeai as genai
# from config import GEMINI_API_KEY

# genai.configure(api_key=GEMINI_API_KEY)

# model = genai.GenerativeModel("gemini-pro")


# def analyze_data(sector: str, news_data):

#     prompt = f"""
# You are a financial market analyst.

# Analyze the following information about the {sector} sector in India.

# News Data:
# {news_data}

# Generate a structured analysis with:

# 1. Market Overview
# 2. Key Trends
# 3. Trade Opportunities
# 4. Potential Risks
# 5. Short Investment Insight

# Keep it concise and professional.
# """

#     response = model.generate_content(prompt)

#     return response.text
# import google.generativeai as genai
# from config import GEMINI_API_KEY

# # Configure Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

# # Load Gemini model
# model = genai.GenerativeModel("gemini-1.5-flash")


# def analyze_data(sector: str, news_data: str):

#     try:

#         # Build prompt for AI analysis
#         prompt = f"""
# You are a financial market analyst.

# Analyze the following information about the {sector} sector in India.

# News Data:
# {news_data}

# Generate a structured analysis with:

# 1. Market Overview
# 2. Key Trends
# 3. Trade Opportunities
# 4. Potential Risks
# 5. Short Investment Insight

# Keep it concise and professional.
# """

#         # Send prompt to Gemini
#         response = model.generate_content(prompt)

#         # If Gemini returns empty result
#         if not response or not response.text:
#             return "AI analysis could not be generated."

#         # Return analysis text
#         return response.text

#     except Exception as e:
#         # Catch errors so API doesn't crash
#         return f"AI analysis failed: {str(e)}"
from google import genai
from config import GEMINI_API_KEY

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_data(sector: str, news_data: str):

    try:

        prompt = f"""
You are a financial market analyst.

Analyze the following information about the {sector} sector in India.

News Data:
{news_data}

Provide:

1. Market Overview
2. Key Trends
3. Trade Opportunities
4. Potential Risks
5. Short Investment Insight
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI analysis failed: {str(e)}"
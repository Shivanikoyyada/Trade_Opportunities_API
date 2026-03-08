import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDKv18SEkt6hEQN75uqylT_FwmwMQN-FBw")

RATE_LIMIT = "5/minute"

VALID_SECTORS = [
    "technology",
    "pharmaceuticals",
    "agriculture",
    "banking",
    "energy"
]
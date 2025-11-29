"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "google/gemini-2.5-flash",      # Good generalist
    "meta-llama/llama-3-8b-instruct",   # Fast and capable
    "mistralai/mistral-7b-instruct",    # Good reasoning
    "microsoft/phi-3-mini-128k-instruct" # High context, lightweight
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "google/gemini-2.5-flash"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"

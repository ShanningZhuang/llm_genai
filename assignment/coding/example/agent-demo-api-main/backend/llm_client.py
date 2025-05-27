import os
import json
import openai

from .config import TIME_OUT, MAX_RETRIES, MODEL, TEMPERATURE, MAX_TOKENS

# Load your API key
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.base_url = os.getenv("OPENAI_API_BASE_URL", "https://api.openai.com/v1")
if openai.api_key is None:
    raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")

api_client = openai.OpenAI(
    api_key=openai.api_key,
    base_url=openai.base_url,
    timeout=TIME_OUT,
    max_retries=MAX_RETRIES
)

# Low-level chat completion wrapper

def llm_request(
    messages: list,
    model: str = MODEL,
    max_tokens: int = MAX_TOKENS,
    temperature: float = TEMPERATURE,
    tools: list = None,
    tool_choice: str = "auto"
) -> openai.ChatCompletion:
    """
    Core ChatCompletion call.
    """
    params = dict(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature
    )
    if tools is not None:
        params["tools"] = tools
        params["tool_choice"] = tool_choice
    return api_client.chat.completions.create(**params)

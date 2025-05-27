from .llm_client import llm_request


def summarize_text(text: str) -> str:
    messages = [
        {"role": "system", "content": "Summarize the following text."},
        {"role": "user", "content": text}
    ]
    resp = llm_request(messages)
    return resp.choices[0].message.content.strip()

def translate_text(text: str, target_language: str) -> str:
    messages = [
        {"role": "system", "content": f"Translate to {target_language}."},
        {"role": "user", "content": text}
    ]
    resp = llm_request(messages)
    return resp.choices[0].message.content.strip()

def extend_text(text: str, max_tokens: int = 150) -> str:
    messages = [
        {"role": "system", "content": "Continue writing the text."},
        {"role": "user", "content": text}
    ]
    resp = llm_request(messages, max_tokens=max_tokens)
    return resp.choices[0].message.content.strip()

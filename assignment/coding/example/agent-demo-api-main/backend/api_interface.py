import json

from .llm_client import llm_request
from .text_utils import summarize_text, translate_text, extend_text
from . import file_tools

# Text operations exposed to user
call_llm    = lambda prompt: llm_request([
    {"role":"system","content":"You are a helpful assistant."},
    {"role":"user","content":prompt}
]).choices[0].message.content.strip()
summarize   = summarize_text
translate   = translate_text
extend      = extend_text

# File operations for model-driven invocation only
file_tools_list = file_tools.tools

# Wrapper to interact, passing file_tools and letting model decide

def interact(prompt: str, messages: list = None) -> str:
    if messages is None:
        messages = [
            {"role":"system","content":"You can use file operations via provided tools."}
        ]
    messages.append({"role":"user","content":prompt})

    while True:
        resp = llm_request(messages, tools=file_tools_list)
        msg = resp.choices[0]
        if msg.finish_reason == 'tool_calls':
            for tool_call in msg.message.tool_calls:
                print(f"Tool call: {tool_call.function}")
                func = tool_call.function
                result = getattr(file_tools, func.name)(**json.loads(func.arguments))
                print(f"Tool result: {str(result)}")
                messages.append(msg.message)
                messages.append({"role":"tool","tool_call_id":tool_call.id,"content":str(result)})
            continue
        print(f"Response: {msg.message}")
        print(f"Finish reason: {msg.finish_reason}")
        messages.append(msg.message)
        return msg.message.content.strip()

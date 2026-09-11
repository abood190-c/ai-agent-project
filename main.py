import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY is not set in the environment variables.")




parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    )

import sys

if args.verbose:
    print(f"# User prompt: {args.user_prompt}")

for _ in range(20):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
    )

    if response.usage is not None:
        if args.verbose:
            print(f"# Prompt tokens: {response.usage.prompt_tokens}")
            print(f"# Response tokens: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("API request failed: usage property is None.")

    message = response.choices[0].message
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            
            if not result_message.get("content"):
                raise Exception("Tool message content cannot be empty")
                
            if args.verbose:
                print(f"-> {result_message['content']}")
                
            messages.append(result_message)
    else:
        print(f"Final response: {message.content}")
        break
else:
    print("Error: Maximum number of iterations (20) reached without a final response.")
    sys.exit(1)
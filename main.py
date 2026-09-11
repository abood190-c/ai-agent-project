import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse



load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY is not set in the environment variables.")




parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "user", "content": args.user_prompt},
]

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    )

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages
)

if response.usage is not None:
    if args.verbose:

        print(f"# User prompt: {args.user_prompt}")
        print(f"# Prompt tokens: {response.usage.prompt_tokens}")
        print(f"# Response tokens: {response.usage.completion_tokens}")
else:
    raise RuntimeError("API request failed: usage property is None.")

print(f"# Response: {response.choices[0].message.content}")
# chat.py
import os
import json
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY not set. Create a .env with OPENAI_API_KEY=<your_key> or set the environment variable.")

with open('knowledge_base.json', 'r') as f:
    knowledge_base = json.load(f)

def ask_gpt(user_input):
    context = '\n'.join([f"{k}: {v}" for k, v in knowledge_base.items()])
    system_prompt = f"You are a helpful customer support agent. Use the following knowledge base to answer questions. If you don't know the answer, say so.\nKnowledge Base:\n{context}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content.strip() 
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Create client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

print("🤖 AI Chatbot (type 'exit' to quit)\n")

# Chat loop
messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = response.choices[0].message.content

    print("AI:", reply)

    messages.append({"role": "assistant", "content": reply})
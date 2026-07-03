from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful assistant named Alex. You are concise and friendly. Always respond in 2-3 sentences max."}
]

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    
    ai_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_reply})
    
    print("AI:", ai_reply)
from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()

MODEL = "google:gemini-2.5-flash" 

SYSTEM_PROMPT = (
    "You are my travel assistant. Help me plan trips, compare options, and build itineraries.\n"
    "Tone: friendly, concise, practical. Keep answers short.\n"
    "Never book, pay for, or confirm anything on my behalf. Suggest options only."
)

agent = Agent(MODEL, system_prompt=SYSTEM_PROMPT)

print("Welcome! I'm your travel assistant. Type 'exit' or 'quit' to leave.")
count = 0

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print(f"Goodbye! We exchanged {count} messages. Safe travels!")
        break
    response = agent.run_sync(user_input)
    count += 1
    print(f"Agent [{count}]: {response.output}")
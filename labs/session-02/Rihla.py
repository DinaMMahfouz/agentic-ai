from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()  

MODEL = "google:gemini-2.5-flash"
AGENT_NAME = "Rihla"

SYSTEM_PROMPT = (
    f"You are {AGENT_NAME}, a travel assistant for leisure travelers planning short trips.\n"
    "Tone: friendly, concise, practical; prefer short bullet lists.\n"
    "Scope: destinations, itineraries, rough budgets, transport options and packing tips.\n"
    "Never book, pay for, or confirm anything on the user's behalf; suggest options only.\n"
    "Never state visa or entry rules as fact; tell the user to verify with the official embassy site.\n"
    "Always respect details the user shared earlier (budget, dates, dietary needs, who is traveling).\n"
    "If a request is outside travel planning or you are not sure, say so and steer back to trip planning."
)

agent = Agent(MODEL, system_prompt=SYSTEM_PROMPT)

print(f"Welcome! I'm {AGENT_NAME}, your travel assistant. Type 'exit' or 'quit' to leave.")
count = 0
history = []  

while True:
    user_input = input("You: ").strip()
    if not user_input: 
        continue
    if user_input.lower() in ["exit", "quit"]:
        print(f"Goodbye! We talked for {count} turns. Safe travels!")
        break
    try:
        result = agent.run_sync(user_input, message_history=history)
    except Exception as e:  
        print(f"{AGENT_NAME}: Sorry, I couldn't reach the AI service ({type(e).__name__}). Please try again.")
        continue
    history = result.all_messages() 
    count += 1
    print(f"{AGENT_NAME} [{count}]: {result.output}")
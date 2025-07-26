from dotenv import load_dotenv
import openai
import os

# Load from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
def ask_agent(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful student assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

print("Welcome to Smart Student Assistant! 🎓")
print("1. Ask a Question")
print("2. Get a Study Tip")
print("3. Summarize a Text")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    question = input("What academic question do you want to ask? ")
    print("\n📘 Answer:")
    print(ask_agent(question))

elif choice == '2':
    print("\n📘 Study Tip:")
    print(ask_agent("Give me a useful study tip"))

elif choice == '3':
    text = input("Paste the paragraph you want summarized:\n")
    print("\n📘 Summary:")
    print(ask_agent(f"Summarize this: {text}"))

else:
    print("Invalid choice.")

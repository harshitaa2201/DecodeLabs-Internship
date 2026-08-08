# -------------------------------------------------
# DecodeLabs AI Project 1
# Rule-Based AI Chatbot
# Created by: Harshita
# -------------------------------------------------

print("=" * 50)
print("🤖 Welcome to Nova AI")
print("Your Friendly Rule-Based AI Assistant")
print("=" * 50)

name = input("Before we begin, what's your name? ")

print(f"\nHello, {name}! 😊")
print("I'm Nova AI. Type 'help' to see what I can do.")
print("Type 'bye' or 'exit' anytime to end the chat.\n")

while True:

    user = input(f"{name}: ").lower()

    if user == "hi" or user == "hello":
        print(f"Nova AI: Hello {name}!👋 Hope you're having a wonderful day!")

    elif user == "good morning":
        print("Nova AI: Good Morning!🌞 Have a productive day ahead!")

    elif user == "good afternoon":
        print("Nova AI: Good Afternoon!😊 Hope your day is going great!")

    elif user == "good evening":
        print("Nova AI: Good Evening!🌇 Relax and enjoy your evening!")

    elif user == "how are you":
        print("Nova AI: I'm doing great! Thanks for asking.😊")

    elif user == "what is your name":
        print("Nova AI: My name is Nova AI, your virtual assistant.")

    elif user == "what is my name":
        print(f"Nova AI: Your name is {name}.")

    elif user == "who created you":
        print("Nova AI: I was created using Python as a part of DecodeLabs Project 1.")

    elif user == "what is ai":
        print("Nova AI: AI stands for Artificial Intelligence.")
        print("It is a branch of computer science that enables machines")
        print("to perform tasks that normally require human intelligence,")
        print("such as learning, reasoning, problem-solving, decision-making,")
        print("understanding language, and recognizing patterns.")

    elif user == "applications of ai":
        print("Nova AI: AI is used in:")
        print("• Virtual Assistants")
        print("• Self-driving Cars")
        print("• Healthcare")
        print("• Online Shopping")
        print("• Banking")
        print("• Gaming")

    elif user == "tell me a joke":
        print("Nova AI: 😂 Why do Python programmers wear glasses?")
        print("Because they can't C!")

    elif user == "fun fact":
        print("Nova AI: 💡 Did you know?")
        print("The first computer bug was an actual moth found inside a computer!")

    elif user == "motivate me":
        print("Nova AI: 💪 Believe in yourself.")
        print("Every expert was once a beginner. Keep learning!")

    elif user == "thank you":
        print("Nova AI: You're most welcome!😊")

    elif user == "help":
        print("\n========== COMMANDS ==========")
        print("hi / hello")
        print("good morning")
        print("good afternoon")
        print("good evening")
        print("how are you")
        print("what is your name")
        print("what is my name")
        print("who created you")
        print("what is ai")
        print("applications of ai")
        print("tell me a joke")
        print("fun fact")
        print("motivate me")
        print("thank you")
        print("bye / exit")
        print("==============================\n")

    elif user == "bye" or user == "exit":
        print(f"\nNova AI: It was wonderful talking to you, {name}!😊")
        print("Goodbye!👋")
        break

    else:
        print("Nova AI: Sorry, I didn't understand that.")
        print("Type 'help' to see the list of available commands.\n")

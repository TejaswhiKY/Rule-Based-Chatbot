import random
import datetime

# -----------------------------
# Rule-Based Chatbot
# -----------------------------

print("=" * 55)
print("        🤖 WELCOME TO RULE-BASED CHATBOT 🤖")
print("=" * 55)
print("Type 'help' to see available commands.")
print("Type 'exit' or 'bye' to quit.\n")

# Greeting responses
greetings = [
    "Hello! 👋 How can I help you today?",
    "Hi there! 😊",
    "Hey! Nice to meet you.",
    "Greetings! What can I do for you?"
]

# Goodbye responses
goodbye = [
    "Goodbye! Have a great day! 😊",
    "Bye! Take care.",
    "See you soon!",
    "Thanks for chatting with me!"
]

# Jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? It had a virus!",
    "Why was the Python developer calm? Because he knew how to handle exceptions!",
    "Why do Java developers wear glasses? Because they don't C#."
]

while True:

    user = input("\nYou : ").strip().lower()

    # -----------------------------
    # Greetings
    # -----------------------------
    if user in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
        print("Bot :", random.choice(greetings))

    # -----------------------------
    # Name
    # -----------------------------
    elif "your name" in user or "who are you" in user:
        print("Bot : I am a Rule-Based Chatbot developed using Python.")

    # -----------------------------
    # Creator
    # -----------------------------
    elif "creator" in user or "who created you" in user:
        print("Bot : I was created as a Python internship project.")

    # -----------------------------
    # How are you
    # -----------------------------
    elif "how are you" in user:
        print("Bot : I'm doing great! Thanks for asking. 😊")

    # -----------------------------
    # Time
    # -----------------------------
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("Bot : Current Time =", current_time)

    # -----------------------------
    # Date
    # -----------------------------
    elif "date" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot : Today's Date =", current_date)

    # -----------------------------
    # Day
    # -----------------------------
    elif "day" in user:
        current_day = datetime.datetime.now().strftime("%A")
        print("Bot : Today is", current_day)

    # -----------------------------
    # Python
    # -----------------------------
    elif "python" in user:
        print("Bot : Python is a powerful, easy-to-learn programming language.")

    # -----------------------------
    # AI
    # -----------------------------
    elif "artificial intelligence" in user or user == "ai":
        print("Bot : Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")

    # -----------------------------
    # Internship
    # -----------------------------
    elif "internship" in user:
        print("Bot : Internship projects help students gain practical skills and experience.")

    # -----------------------------
    # College
    # -----------------------------
    elif "college" in user:
        print("Bot : I hope your college journey is going well!")

    # -----------------------------
    # Weather
    # -----------------------------
    elif "weather" in user:
        print("Bot : Sorry! I cannot access live weather information.")

    # -----------------------------
    # Joke
    # -----------------------------
    elif "joke" in user:
        print("Bot :", random.choice(jokes))

    # -----------------------------
    # Calculator
    # -----------------------------
    elif user == "calculator":
        print("\nSimple Calculator")
        print("-----------------")
        print("Example: 25+10")
        print("Example: 100/5")
        print("Example: 8*9")

        expression = input("Enter Expression: ")

        try:
            result = eval(expression)
            print("Bot : Answer =", result)
        except:
            print("Bot : Invalid Expression!")

    # -----------------------------
    # Help
    # -----------------------------
    elif user == "help":

        print("\nAvailable Commands")
        print("-----------------------------")
        print("hi")
        print("hello")
        print("how are you")
        print("your name")
        print("creator")
        print("time")
        print("date")
        print("day")
        print("python")
        print("ai")
        print("internship")
        print("college")
        print("weather")
        print("joke")
        print("calculator")
        print("help")
        print("exit")

    # -----------------------------
    # Thanks
    # -----------------------------
    elif "thank" in user:
        print("Bot : You're welcome! 😊")

    # -----------------------------
    # Exit
    # -----------------------------
    elif user in ["bye", "exit", "quit"]:

        print("Bot :", random.choice(goodbye))
        print("\nChatbot Closed Successfully.")
        break

    # -----------------------------
    # Unknown Input
    # -----------------------------
    else:
        print("Bot : Sorry, I don't understand that.")
        print("Bot : Type 'help' to see the available commands.")
# ===========================================
# 🤖 BASIC RULE-BASED CHATBOT
# ===========================================

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hii", "hey"]:
        return "Hi! 👋 How can I help you today?"

    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great! 😊 How about you?"

    elif user_input in ["what are you doing", "what are you doing now"]:
        return "I'm here to assist you with your queries 🤖"

    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple chatbot created using Python!"

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! 😊"

    elif user_input in ["good morning"]:
        return "Good morning! 🌅 Have a great day!"

    elif user_input in ["good afternoon"]:
        return "Good afternoon! ☀️"

    elif user_input in ["good evening"]:
        return "Good evening! 🌇"

    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! 👋 Have a nice day!"

    elif user_input in ["help"]:
        return "I can respond to greetings, basic questions, and conversations."

    elif user_input in ["what can you do"]:
        return "I can chat with you and answer basic questions!"

    elif user_input in ["are you human"]:
        return "No, I'm a chatbot created using Python 🤖"

    elif user_input in ["where are you from"]:
        return "I exist inside your computer 😄"

    elif user_input in ["what is python"]:
        return "Python is a popular programming language used for many applications."

    elif user_input in ["tell me a joke"]:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 😄"

    else:
        return "Sorry, I didn't understand that. Try asking something else."

# -------------------------------
# Main Chat Loop
# -------------------------------
print("===================================")
print("🤖 BASIC CHATBOT")
print("Type 'bye' to exit")
print("===================================")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower() in ["bye", "goodbye", "see you"]:
        break

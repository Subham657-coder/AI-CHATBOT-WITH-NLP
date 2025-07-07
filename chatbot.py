import nltk
import random
import string


responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm just a program, but I'm doing great!", "All systems operational."],
    "what is your name": ["I am a chatbot created using Python.", "You can call me ChatBot!"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase it?", "I'm not sure I understand."]
}

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    return tokens

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

print("🤖 ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("🧑 You: ")
    if 'bye' in user_input.lower():
        print("🤖 ChatBot:", random.choice(responses["bye"]))
        break
    response = get_response(user_input)
    print("🤖 ChatBot:", response)

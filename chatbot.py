import re
import nltk
from nltk.tokenize import word_tokenize
from chatbot_data import responses
import logging
import os

nltk.download('punkt')
logging.basicConfig(filename='chat_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_interaction(user_input, bot_response):
    logging.info(f"User: {user_input}\nBot: {bot_response}")

def get_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    
    for pattern, response in responses.items():
        if any(re.search(pattern, token) for token in tokens):
            return response
    
    return f"{responses.get('default', 'Sorry, I do not understand that question.')} {suggest_questions()}"

def suggest_questions():
    return "Here are some basic questions you can ask me: 'What are your hobbies?', 'What is your educational background?', Also you can respond with 'help' for a list of all keywords I am programmed to answer."

def main():
    print("Hello! My name is Colby, an artificial construct made by Colby to be as close to the real thing as possible!")
    print(suggest_questions())
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye for now!")
            break
        
        response = get_response(user_input)
        print(f"Colby: {response}")
        log_interaction(user_input, response)

if __name__ == "__main__":
    main()

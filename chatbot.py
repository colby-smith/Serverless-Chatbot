import re
import nltk
from nltk.tokenize import word_tokenize
from chatbot_data import responses
nltk.download('punkt')

def log_interaction(user_input, bot_response):
    with open('chat_log.txt', 'a') as log_file:
        log_file.write(f"User: {user_input}\n")
        log_file.write(f"Bot: {bot_response}\n\n")

def get_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    
    for pattern, response in responses.items():
        if any(re.search(pattern, token) for token in tokens):
            return response
    
    return f"{responses.get('default', 'Sorry, I don\'t understand that question.')} {suggest_questions()}"

def suggest_questions():
    return "Here are some basic questions you can ask me: 'What are your hobbies?', 'What is your educational background?', Also you can respond with 'help' for a list of all keywords I am programmed to answer."

def main():
    print("Hello! My name is Colby, an artifical construct made by Colby to be as close to the real thing as possible!")
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

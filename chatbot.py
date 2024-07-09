import re
from chatbot_data import responses

def get_response(user_input):
    user_input = user_input.lower()
    
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
    
    return responses.get("default", "Sorry, I don't understand that question.")

def suggest_questions():
    return "Here are some basic questions you can ask me: 'What are your hobbies?', 'What is your educational background?'"

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

if __name__ == "__main__":
    main()

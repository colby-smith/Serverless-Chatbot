import re
from chatbot_data import responses

def get_response(user_input):
    user_input = user_input.lower()

    if "name" in user_input:
        return responses["name"]
    elif "hobbies" in user_input:
        return responses["hobbies"]
    elif "education" in user_input:
        return responses["education"]
    else:
        return responses["default"]

def main():
    print("Hello! My name is Colby, an artifical construct made by Colby to be as close to the real thing as possible. Ask me anything you'd like to know about Colby!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye for now!")
            break
        response = get_response(user_input)
        print(f"Colby: {response}")

if __name__ == "__main__":
    main()

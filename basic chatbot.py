def get_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I'm sorry, I only understand 'hello', 'how are you', and 'bye'."

def start_chatbot():
    print("--- Basic Chatbot ---")
    
    while True:
        user_message = input("You: ")
        response = get_response(user_message)
        print(f"Chatbot: {response}")
        
        if user_message.lower() == "bye":
            break

if __name__ == "__main__":
    start_chatbot()

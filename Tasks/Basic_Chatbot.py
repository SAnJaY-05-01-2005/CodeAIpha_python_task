def get_bot_response(user_input):
    """
    This function takes the user's text, checks for keywords,
    and returns the appropriate bot response.
    """
    # 1. PRE-PROCESSING: Convert input to lowercase for easier matching
    # This ensures "Hello", "hello", and "HELLO" are treated the same.
    cleaned_input = user_input.lower().strip()

    # 2. LOGIC: Check for keywords using if-elif-else
    if "hello" in cleaned_input or "hi" in cleaned_input:
        return "Hello there! It's nice to meet you."
    
    elif "how are you" in cleaned_input:
        return "I'm just a computer program, but I'm functioning perfectly! Thanks for asking."
    
    elif "name" in cleaned_input:
        return "I am PythonBot v1.0."
    
    elif "bye" in cleaned_input or "exit" in cleaned_input:
        return "Goodbye! Have a great day."
        
    else:
        # 3. FALLBACK: What to say if we don't understand
        return "I'm sorry, I don't understand that yet. Try saying 'Hello' or 'How are you'."

def start_chat():
    print("--- Simple Python Chatbot ---")
    print("Type 'bye' to exit the chat.\n")

    # 4. LOOP: Keep the program running indefinitely
    while True:
        # Get input from user
        user_text = input("You: ")

        # Get response from our function
        bot_reply = get_bot_response(user_text)

        # Print the bot's reply
        print(f"Bot: {bot_reply}")

        # Check if the user wants to quit
        # We look at the reply to see if it's the goodbye message
        if "Goodbye" in bot_reply:
            break

# Run the chatbot
start_chat()
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "refund" in user_input:
        return "To process a refund, please provide your order ID."
    elif "contact" in user_input:
        return "You can contact our support team at support@example.com."
    elif "thank" in user_input:
        return "You're welcome! If you have more questions, feel free to ask."
    else:
        return "I'm still learning. Could you please rephrase your question?"

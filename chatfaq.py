faq_data = {
    "price of the mobile?": "The price is 20000",
    "how long is the battery life?": "The battery can with stand up to 10 hours",
    "How can I contact customer service?": "You can contact customer service at support@example.com or call 123-456-7890.",
    "What is your return policy?": "Our return policy allows returns within 30 days of purchase with a receipt.",
    "Do you offer international shipping?": "Yes, we offer international shipping to most countries. Additional charges may apply."
}

def chatbot(question):
    # Iterate through the FAQ data to find a matching question
    for faq_question, answer in faq_data.items():
        if question.lower() in faq_question.lower():
            return answer
    return "I'm sorry, I don't have an answer for that. Can you please ask another question?"

def main():
    print("Welcome to the FAQ Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chatbot(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
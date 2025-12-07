import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        r"\b(1|hello|hi|hey)\b": "Hello! Welcome to our grocery store. How can I assist you today?",
        r"\b(2|how are you)\b": "I'm just a bot, but I'm ready to help you with anything you need.",
        r"\b(3|order status|track order)\b": "Sure, please share your order ID and I'll check the status for you.",
        r"\b(4|shipping time|delivery time)\b": "We offer same-day delivery in some areas, and standard shipping usually takes 3 to 5 business days.",
        r"\b(5|return policy)\b": "You can return unopened items within 7 days of purchase. Would you like to start a return?",
        r"\b(6|thank you|thanks)\b": "You're welcome! Let me know if there's anything else I can help you with.",
        r"\b(7|price|cost)\b": "Please tell me the product name so I can give you its price.",
        r"\b(8|milk)\b": "Milk is priced at 30 rupees per liter.",
        r"\b(9|eggs)\b": "A dozen eggs cost 80 rupees.",
        r"\b(10|rice)\b": "Rice is available at 50 rupees per kilogram.",
        r"\b(11|vegetables|veggies)\b": "We have a variety of fresh vegetables. What would you like to know about?",
        r"\b(12|fruits)\b": "We have apples, bananas, and oranges available. Which one are you looking for?",
        r"\b(13|snacks)\b": "We have chips, biscuits, and chocolates in stock. Would you like details on any of these?",
        r"\b(14|beverages|drinks)\b": "We offer soft drinks, juices, and bottled water. What are you looking for?",
        r"\b(15|buy|order)\b": "You can place your order through our website or by visiting our store.",
        r"\b(16|payment methods|payment)\b": "We accept cash, credit and debit cards, as well as UPI payments.",
        r"\b(17|store hours|timing)\b": "Our store is open every day from 8 AM to 10 PM.",
        r"\b(18|location|address)\b": "Our store is located at XYZ Market, Main Street, YourCity.",
        r"\b(19|bye|exit)\b": "Goodbye! Thank you for visiting. Have a great day."
    }

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
   
    return "I'm sorry, I didn't understand that. Could you please rephrase or ask about a specific grocery item?"

# Chatbot interaction loop
print("Welcome to our Grocery Chatbot! Type 'exit' to end the conversation.\n")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Thank you for shopping with us.")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)
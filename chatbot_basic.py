
def chatbot():
    print("SupportBot (type exit to quit)")
    while True:
        msg = input("You: ").lower()
        if msg == "exit":
            break
        if "hello" in msg:
            print("Bot: Hello!")
        elif "refund" in msg:
            print("Bot: Refunds take 5–7 days.")
        else:
            print("Bot: Please rephrase.")
chatbot()

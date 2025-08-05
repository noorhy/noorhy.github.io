class SimpleAIAgent:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I help you today?",
            "hi": "Hi there! What can I do for you?",
            "bye": "Goodbye! Have a nice day!",
            "name": "I'm your simple AI agent.",
            "help": "I can answer simple greetings and tell you my name."
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for keyword, response in self.responses.items():
            if keyword in user_input:
                return response
        return "Sorry, I don't understand. Can you rephrase?"

if __name__ == "__main__":
    agent = SimpleAIAgent()
    print("Simple AI Agent. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = agent.get_response(user_input)
        print("AI:", response)
        if "bye" in user_input.lower():
            break
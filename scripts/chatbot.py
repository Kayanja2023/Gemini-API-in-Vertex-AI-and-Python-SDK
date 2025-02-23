import openai

def chat_with_ai():
    
    """ This script runs an interactive chatbot using OpenAI's GPT model where the user inputs messages, and the AI responds."""
    openai.api_key = "your-api-key"
    print("AI Chatbot - Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        
        print("Chatbot:", response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    chat_with_ai()

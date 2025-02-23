import openai

# Set up API Key
openai.api_key = "your-api-key"

def generate_text(prompt):
    """Generates AI-powered text based on a given prompt."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    output = generate_text(prompt)
    print("\nAI Generated Response:")
    print(output)

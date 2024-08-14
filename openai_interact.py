import openai

# Directly set your API key here (for testing purposes only)
openai.api_key = 'WRITE Your API HERE'

def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the updated model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except openai.error.AuthenticationError:
        return "Authentication error: Please check your API key."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    if not openai.api_key:
        print("API Key: None")
        return

    user_input = input("You: ")
    response = get_openai_response(user_input)
    print("AI:", response)

if __name__ == "__main__":
    main()

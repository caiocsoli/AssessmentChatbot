import openai

openai.api_key = "sk-51EFRplDiCXzrVWv9j9TT3BlbkFJY2Q25uPWakOHSNbTCvo8Y"

def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']

conversation = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke."}]

response = generate_response(conversation)
print(response)


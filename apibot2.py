from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input = input("you: ")
    if user_input == "quit":
        print("bot: Goodbye!")
        break

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a medical bot, provide information only related to medical queries."},
            {"role": "user", "content": user_input}
        ]
    )

    print("bot: ", response.choices[0].message.content)

import openai

# https://platform.openai.com/docs/models/gpt-3
# leaving free some tokens for prompt
best = ('text-davinci-003', 3900)   # Most capable GPT-3 model
good = ('text-curie-001', 1900)     # Very capable, but faster and lower cost than Davinci.
fast = ('text-ada-001', 1900)       # Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost.

def ask_chatgpt(prompt):
    model = best
    response = openai.Completion.create(engine=model[0], prompt=prompt, max_tokens=model[1])
    print(response.choices[0].text)


while True:
    user_input = input("\nPrompt: ")
    if user_input.lower() == "end":
        break
    prompt = f"AI-boi: {user_input}\nYou:"
    ask_chatgpt(prompt)


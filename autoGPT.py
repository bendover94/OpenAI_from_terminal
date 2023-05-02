import openai

# https://platform.openai.com/docs/models/gpt-3
# leaving free some tokens for prompt
best = ('text-davinci-003', 3900)   # Most capable GPT-3 model
good = ('text-curie-001', 1900)     # Very capable, but faster and lower cost than Davinci.
fast = ('text-ada-001', 1900)       # Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost.

def agent_1(prompt):
    model = best
    response = openai.Completion.create(engine=model[0], prompt=prompt, max_tokens=model[1])
    answer_text = response.choices[0].text
    print(f"Agent 1: {answer_text}")
    return answer_text


def agent_2(answer_agent_1):
    model = best
    response = openai.Completion.create(engine=model[0], prompt=answer_agent_1, max_tokens=model[1])
    answer_text = response.choices[0].text
    print(f"Agent 2: {answer_text}")
    answer_text = "Can you please be more precise in elaborating: " + answer_text
    return answer_text


while True:
    user_input = input("\nPrompt: ")    # initial taking user prompt

    prompt = f"AI-boi: {user_input}\nYou:"
    answer_agent = agent_1(prompt)      # feeding prompt to initial agent

    while True:
        user_input = input("\nHit 'q' to stop.")    # escape condition via user input
        if user_input.lower() == 'q':
            break
        else:
            answer_agent = agent_2(answer_agent)    # if not escaped, optimize output until 'q' is pressed



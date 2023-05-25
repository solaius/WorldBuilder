import openai
from constants import chatgpt_api_key, chatgpt_model_default

def gpt_turbo_query(system_role, user_prompt):
    openai.api_key = chatgpt_api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Replace with the correct engine
        messages=[
            {
                "role": "system",
                "content": system_role,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]
    )

    return response.choices[0].message['content']


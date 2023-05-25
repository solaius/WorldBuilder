import openai

# Your OpenAI API key
openai.api_key = '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'

# The setting for the world builder assistant to use
setting = "Grimbriar, a homebrew Dungeons and Dragons 5e Ravenloft Domain of Dread, Made up of a large cemetary, a small village and a large stone tower where the lord of Grimbriar resides, mad scientist and wizard, Dr. Leopold Moonshade"

# Expected format of the response
prompt_response_format = "firstname,lastname,class,alignment,profession,age,spousename,background,current status /n"

# User prompt that will be sent to the assistant
user_prompt = "Generate 5 NPCs using the format:" + prompt_response_format + "/n/n" + "In the following setting:" + setting + "|Make sure to interweave their backgrounds together and their fear of their lord and master.|Then make a paragraph about the past few years of them living in fear of Leopold's experiments"

# Role of the assistant
system_role = "You are a world building assistant in the following setting: " + setting

# Messages for first assistant
messages = [
    {"role": "system", "content": system_role},
    {"role": "user", "content": user_prompt},
]

def ask_gpt3(messages):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    # The assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply

# Get responses from both assistants
response1 = ask_gpt3(messages)
print("Assistant 1:", response1)

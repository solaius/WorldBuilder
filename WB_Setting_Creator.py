import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data/world_builder.db')
cursor = conn.cursor()

# Setting Types
cursor.execute("SELECT * FROM Setting_Types")
rows = cursor.fetchall()
setting_types = []
for row in rows:
    setting_types.append(row[0])  

# Setting Subtypes
cursor.execute("SELECT * FROM Setting_SubTypes")
rows = cursor.fetchall()
setting_subtypes = []
for row in rows:
    setting_subtypes.append(row[0])  

# Setting Tones
cursor.execute("SELECT * FROM Setting_Tones")
rows = cursor.fetchall()
setting_tones = []
for row in rows:
    setting_tones.append(row[0])

# Setting Sizes
cursor.execute("SELECT * FROM Setting_Sizes")
rows = cursor.fetchall()
setting_sizes = []
for row in rows:
    setting_sizes.append(row[0])  

# Close the cursor and the connection
cursor.close()
conn.close()

setting_elements = {
    "setting_type": setting_types,
    "setting_subtype": setting_subtypes,
    "setting_tone": setting_tones,
    "setting_size": setting_sizes,
    "setting_description": "",
    "setting_name": "",
    "setting_negative_prompt": "",
}

def submit_setting(setting_name, setting_type, setting_subtype, setting_tone, setting_size, setting_description, negative_description):
    # Generate prompt based on the form inputs
    prompt = f"Create a ficticious setting for a role playing game with the following details:\n\n"  

    if setting_name:
        prompt += f" for '{setting_name}'"

    prompt += " with the following details:\n\n"

    if setting_type:
        prompt += f"Setting Type: {setting_type}\n"

    if setting_subtype:
        prompt += f"Setting Subtype: {setting_subtype}\n"

    if setting_tone:
        prompt += f"Story Tone: {setting_tone}\n"

    if setting_size:
        prompt += f"Size: {setting_size}\n\n"

    if setting_description:
        prompt += f"Setting Description: {setting_description}\n\n"

    if negative_description:
        prompt += f"Negative Description: {negative_description}\n\n"

    prompt += "Please use your creativity to develop an engaging and immersive setting."

    # Use the generated prompt to pass it to GPT for further processing

    return 
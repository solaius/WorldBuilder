# World Builder Database
wb_db_path = "data/world_builder.db"

# ChatGPT API Key
chatgpt_api_key = "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"

# ChatGPT Model
chatgpt_model_default = "gpt-3.5-turbo"
chatgpt_models = [
    "gpt-4",
    "gpt-3.5-turbo"
]
chatgpt_system_role_prefix = "World building assistant in the following setting: "

# Error Messages
class ErrorCodes:
    INVALID_INPUT = 100
    MISSING_FIELD = 101
    SERVER_ERROR = 500
    DATABASE_ERROR = 501

class ErrorMessages:
    INVALID_INPUT = "Invalid input. Please check your form data."
    MISSING_FIELD = "One or more required fields are missing."
    SERVER_ERROR = "An unexpected server error occurred."
    DATABASE_ERROR = "A database error occurred."

# test setting prompts
setting_ravenloft = "Grimbriar, a homebrew Dungeons and Dragons 5e Ravenloft Domain of Dread, Made up of a large cemetary, a small village and a large stone tower where the lord of Grimbriar resides, mad scientist and wizard, Dr. Leopold Moonshade"
setting_cyberpunk = "Neo-Tokyo 220X is a sprawling megacity of neon-lit streets, towering skyscrapers, and cybernetically enhanced inhabitants. Corporate mega-corporations rule over the city, exploiting its denizens and monopolizing advanced technologies. Underground augmentations, illegal netrunning, and shady dealings dominate the city's shadowy underbelly. Corruption runs deep, and rebels fight to expose the truth and reclaim the city from the clutches of corporate tyranny."
setting_pirate = "Crimson Tide is a treacherous and lawless archipelago, infested with notorious pirate crews and hidden treasures. Turquoise waters teem with menacing sea creatures, while rugged islands harbor hidden coves and treacherous caves. Pirate captains command their vessels, engaging in high-stakes battles and daring raids. A constant struggle for power and riches permeates the salty air, as pirates navigate a perilous world where alliances shift like the tides."
setting_space = "Stellaris Station is a colossal space station located at the edge of the known universe. Its gleaming metallic structure houses a diverse array of alien species, united in their pursuit of interstellar exploration and diplomacy. Intergalactic trade thrives within its bustling marketplaces, while vast hangars launch starships to chart uncharted territories. Amidst the vast expanse of space, Stellaris Station serves as a beacon of unity and cooperation among the stars."
test_settings_prompts = [setting_ravenloft, setting_cyberpunk, setting_pirate, setting_space]
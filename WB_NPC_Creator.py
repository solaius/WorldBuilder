import random  
import gpt.gpt_3T

# The setting for the world builder assistant to use
setting = "Grimbriar, a homebrew Dungeons and Dragons 5e Ravenloft Domain of Dread, Made up of a large cemetary, a small village and a large stone tower where the lord of Grimbriar resides, mad scientist and wizard, Dr. Leopold Moonshade"

# Expected format of the response
prompt_response_format = "firstname,lastname,class,alignment,profession,age,spousename,background,current status /n"

# User prompt that will be sent to the assistant
user_prompt = "Generate 5 NPCs using the format:" + prompt_response_format + "/n/n" + "In the following setting:" + setting + "|Make sure to interweave their backgrounds together and their fear of their lord and master.|Then make a paragraph about the past few years of them living in fear of Leopold's experiments"

# Role of the assistant
system_role = "You are a world building assistant in the following setting: " + setting


# Lists of possible attributes
races = ["Human", "Elf", "Dwarf", "Halfling"]
classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
professions = ["Blacksmith", "Baker", "Innkeeper", "Farmer", "Fisherman", "Carpenter", "Herbalist", "Hunter", "Tavern Owner", "Tailor", "Miner", "Priest", "Miller", "Barber", "Weaver", "Scribe", "Guard", "Stablehand", "Jeweler", "Fletcher"]
family_names = ["Hawthorne", "Blackwood", "Ravenscroft", "Grimm", "Shadowborne", "Mistwood", "Wraithborne", "Ashthorn", "Nightshade", "Moonbrook"]
npc_age = range(20, 70)

# NPC Generator function
def generate_npc():
    npc = {}

    # Generate random attributes
    npc["race"] = random.choice(races)
    npc["class"] = random.choice(classes)
    npc["profession"] = random.choice(professions)
    npc["level"] = random.randint(0, 5)
    npc["age"] = random.randint(20, 70)
    # Add additional attributes as needed
    # npc["name"] = generate_random_name()
    # npc["alignment"] = generate_random_alignment()

    return npc

# Generate a random NPC
random_npc = []

for _ in range(10):
    npc = generate_npc()
    random_npc.append(npc)

# Print the NPC's attributes
for npc in random_npc:
    print("Race:", npc["race"])
    print("Class:", npc["class"])
    print("Profession", npc["profession"])
    print("Level:", npc["level"])
    print("Age:", npc["age"])

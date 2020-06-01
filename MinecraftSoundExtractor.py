print("Starting...") # Opening message

# Import stuffs used
import os
import json
from shutil import copy2

# Minecraft assets directory
MINECRAFT_DIR = os.getenv('APPDATA')+"/.minecraft/assets/"

# Method to extract music or sounds.
def extractObj(type):
    for obj in type:
        if type.index(obj) % 2 == 1:
            path = MINECRAFT_DIR + "objects/" + str(obj[:2]) + "/" + obj
            dest = "out/" + version + "/" + type[type.index(obj) - 1]
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            copy2(path, dest)
            print("Copied file: " + type[type.index(obj) - 1])

rawInputFiles = os.listdir(MINECRAFT_DIR+"indexes") # Retrieve available files, as [version].json
inputFiles = [] # Stores the versions of the files we can use

# Loop through the available versions, store them in inputFiles, and print them
print("\nAvailable versions:")
for file in rawInputFiles:
    inputFiles.append(file.strip(".json"))
    print(file.strip(".json"))

# Ask what version of Minecraft to extract sounds from
version = input("\nPlease type in the version you want to extract sounds from: ").lower()
while not version in inputFiles:
    print("Invalid option.")
    version = input("\nPlease type in the version you want to extract sounds from: ").lower()

# Ask whether to extract music, sound effects, or both
request = input("\nPlease type in whether you want music, sound effects, or both.\nAnswer with one of these: music, sfx, both: ").lower()
while not request in ["music", "sfx", "both"]:
    print("Invalid option.")
    request = input("\nPlease type in whether you want music, sound effects, or both.\nAnswer with one of these: music, sfx, both: ").lower()

sounds = [] # Will contain paths and hashes for sfx
music = [] # Will contain paths and hashes for music

# Store the paths and hashes for music and sfx
data = json.load(open(MINECRAFT_DIR+"indexes/"+version+".json", 'r'))
for x in data["objects"]:
    if x[:17] == "minecraft/sounds/" and not x[:23] == "minecraft/sounds/music/":
        sounds.append(x)
        sounds.append(data["objects"][x]["hash"])
    elif x[:23] == "minecraft/sounds/music/":
        music.append(x)
        music.append(data["objects"][x]["hash"])

# Extract files
if not request == "music":
    print("\nExtracting sounds...")
    extractObj(sounds)
if not request == "sfx":
    print("\nExtracting music...")
    extractObj(music)
    print("\nMusic is in \'out/"+version+"/minecraft/sounds/music\'.") # Clarify where music is located

print("\nDone!") # Closing message
os.system('pause')
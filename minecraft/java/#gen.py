# !!! BEFORE RUNNING !!!
# Download the latest server.jar and place it into the directory with this script. 

# Generates all json lists using the registries.json from the built-in data generator: https://minecraft.wiki/w/Tutorials/Running_the_data_generator

import os
import json
import mcextract
import shutil

MCVERSION = '1.21'
LOCAL = os.path.dirname(os.path.realpath(__file__))
TEMP = os.path.join(LOCAL, 'temp')

# Get registry
api = mcextract.MCExtractAPI()
api.generate('server.jar', ['--reports'], TEMP, True)

with open(os.path.join(TEMP, 'reports', 'registries.json'), 'r') as fd:
    registries = json.load(fd)

with open(os.path.join(LOCAL, 'registries.json'), 'w') as fd:
    fd.write(json.dumps(registries))

shutil.rmtree(TEMP)

opn = open(LOCAL + "/registries.json", "r")
registries = json.load(opn)
opn.close()

README = f"""# README

Feel free to reference these for your schemas. They will contain up-to-date lists of items, blocks, effects, sounds, etc.

Updated for `{ MCVERSION }`

## References

| Name | Raw URL |
| -- | -- |
"""

for registry in registries:
    print(registry)
    filename = registry.replace("minecraft:", "")
    title = filename.title().replace("/", "").replace("_", " ")

    # README += f"### [{title}]({filename}.json)\n\nA complete list of all {title} ID's. \n\n```txt\nhttps://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/minecraft/java/{filename}.json\n```\n\n***\n\n"""
    README += f"| [{title}](./{filename}.json) | `https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/minecraft/java/{filename}.json` |\n"

    schema = {
        "$id": f"https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/minecraft/java/{filename}.json",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "string",
        "pattern": "^[a-zA-Z0-9._]*.:.[a-zA-Z0-9._]*$",
        "description": f"Any Minecraft {title} (Java Edition)",
        "examples": [],
    }

    for item in registries[registry]["entries"]:
        print("-", item)
        schema["examples"].append(item)

    dir = os.path.dirname(filename + ".json")
    os.makedirs(os.path.join(LOCAL, dir), exist_ok=True)

    with open(os.path.join(LOCAL, filename + ".json"), "w") as fd:
        fd.write(json.dumps(schema, indent=4))

with open(LOCAL + "/README.md", "w") as fd:
    fd.write(README)

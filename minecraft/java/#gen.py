# Generates all json lists using the registries.json from the built-in data generator: https://minecraft.wiki/w/Tutorials/Running_the_data_generator
# TODO: Use mcextract API
import os
import json

LOCAL = os.path.dirname(os.path.realpath(__file__))

opn = open(LOCAL + "/registries.json", "r")
registries = json.load(opn)
opn.close()

opn = open(LOCAL + "/README.md", "r")
README = opn.read()
opn.close()

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

    wrt = open(os.path.join(LOCAL, filename + ".json"), "w")
    wrt.write(json.dumps(schema, indent=4))
    wrt.close()

wrt = open(LOCAL + "/README.md", "w")
wrt.write(README)
wrt.close()

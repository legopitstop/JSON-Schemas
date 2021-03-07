# **INFO**
## [What are Schemas?](https://json-schema.org/understanding-json-schema/about.html)
Schemas are JSON files that will help and aid you in creating your code and
will show you any errors that will come up when loading up your mod. A good example
is the Minecraft Bedrock Addon Schemas. If you have that schema installed in VSC it will help
you by suggesting things to be added into the code. It also provides useful tooltips when you hover over the text to tell you what it does.

Join my discord to get live updates on schemas. [Discord](https://discord.gg/JbyTHWW)
<br>
[View Update Log](UPDATES.md)

## Screenshots

![img](https://cdn.discordapp.com/attachments/786714100205092915/789987247830335508/image.png "Schemas provide useful tool tips to better understand what parameters do what.")

![img](https://cdn.discordapp.com/attachments/786714100205092915/789987365791727646/image_1.png "It suggests parameters as you type.")

![img](https://cdn.discordapp.com/attachments/786714100205092915/789987943900512306/image_2.png "Alerts you if its missing a required bit of code.")

## How to Install *Visual Studio Code*
1. Open VSC. 
2. Go to your settings ( `CTRL` + `,` )
3. At the top corner you should find a button that will open settings (JSON). Click it.
4. Paste the below code into that JSON.
5. Save it. Thats it your done!

**MORE NBT DATAPACK**

```json
{
    "json.schemas": [
        {
            "fileMatch": [
                "*.json"
            ],
            "url": "https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/more%20NBT%20Datapack%20Schemas/schema.json"
        }
    ]
}
```
**BEDROCK ADDON SCHEMAS**
```json
{
    "json.schemas": [
        {
            "name": "Bedrock Edition Schema",
            "description": "Schema for Bedrock Edition behavior, and resourcepacks.",
            "fileMatch": [
                "com.mojang/development_behavior_packs/*.json",
                "com.mojang/development_resource_packs/*.json",
                "com.mojang/behavior_packs/*.json",
                "com.mojang/resource_packs/*.json"
            ],
            "url": "https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/schemas/bedrock-edition-schema/schema.json"
        }
    ]
}
```
**JAVA EDITION SCHEMAS**
```json
{
    "json.schemas": [
        {
            "name": "Java Edition Schema",
            "description": "Loot Tables",
            "fileMatch": [
                "data/*/loot_tables/*/*.json"
            ],
            "url": "https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/schemas/java-edition-schema/draft-01/loot_tables/schema.json"
        },
        {
            "name": "Java Edition Schema",
            "description": "Item Models",
            "fileMatch": [
                "assets/*/models/item/*.json",
                "assets/*/models/items/*.json"
            ],
            "url": "https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/schemas/java-edition-schema/draft-01/item-models/schema.json"
        },
        {
            "name": "Java Edition Schema",
            "description": "Block Models",
            "fileMatch": [
                "assets/*/models/block/*.json",
                "assets/*/models/blocks/*.json"
            ],
            "url": "https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/schemas/java-edition-schema/draft-01/block-models/schema.json"
        },
        {
            "name": "Java Edition Schema",
            "description": "Schema for Java Edition datapack and resourcepacks.",
            "fileMatch": [
                "*.json"
            ],
            "url": "https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/schemas/java-edition-schema/draft-01/schema.json"
        }
    ]
}
```

# [**UPDATES**](UPDATES.md#)
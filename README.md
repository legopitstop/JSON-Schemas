# **INFO**
## [What are Schemas?](https://json-schema.org/understanding-json-schema/about.html)
Schemas are JSON files that will help and aid you in creating your code and
will show you any errors that will come up when loading up your mod. A good example
is the Minecraft Bedrock Addon Schemas. If you have that schema installed in VSC it will help
you by suggesting things to be added into the code. It also provides useful tooltips when you hover over the text to tell you what it does.

Join my discord to get live updates on schemas. [Discord](https://discord.gg/JbyTHWW)

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

# **UPDATES**
Get Live updates via my [discord server](https://discord.gg/JbyTHWW)

## Logs
### (12/10/2020)
Minecraft Bedrock schema was just released. Find the code in the `#schemas-install` channel

### (12/10/2020)
Update to `Bedrock Addon Schemas` added support for more components, including entities, recipes, etc

### (01/20/2021)
Bunch of other updates including updating for beta 1.16.210.56 added `"ignore_game_mode"` for block event responcse `"decresement_stack"`, set to false by default. Thus `"decrement_stack"` no longer decreases the item stack when playing in Creative by default .
https://feedback.minecraft.net/hc/en-us/articles/360055733571

### (02/03/2021)
Updates for beta 1.16.210.58. added `"minecraft:render_offsets"` to data driven items. made `"format_version"` take in any string, number instead of enum. it will still recomend common versions.
https://feedback.minecraft.net/hc/en-us/articles/360056026212

### (03/03/2021)
Added `Java Edition Schemas`
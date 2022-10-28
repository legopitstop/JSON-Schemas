# INFO

## [What are Schemas?](https://json-schema.org/understanding-json-schema/about.html)

Schemas are JSON files that will help and aid you in creating your code and
will show you any errors that will come up when loading up your mod. A good example
is the Minecraft Bedrock Addon Schemas. If you have that schema installed in VSC it will help
you by suggesting things to be added into the code. It also provides useful tooltips when you hover over the text to tell you what it does.

Join my discord to get live updates on schemas. [Discord](https://discord.gg/JbyTHWW)
<br>
[View Update Log](UPDATES.md)

## How to Install schema for *Visual Studio Code*

1. Open VSC. 
2. Go to your settings ( `CTRL` + `,` )
3. At the top corner you should find a button that will open settings (JSON). Click it.
4. Paste the below code into that JSON.
5. Save it. Thats it you're done!

```json
{
    "json.schemas": [
        // append below code here.
    ]
}
```

### [Minecraft Bedrock Edition](https://minecraft.fandom.com/wiki/Bedrock_Edition)

```json
{
    "name": "Bedrock Edition Schema",
    "description": "Schema for Bedrock Edition behavior, and resourcepacks.",
    "fileMatch": [
        "com.mojang/**.json"
    ],
    "url": "https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/schemas/bedrock/schema.json"
}
```

### [Minecraft Java Edition](https://minecraft.fandom.com/wiki/Java_Edition)

```json
{
    "name": "Java Edition Schema",
    "description": "Advancements",
    "fileMatch": [
        "data/*/advancements/*/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/advancements/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "dimension",
    "fileMatch": [
        "data/*/dimension/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/dimension/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "dimension_type",
    "fileMatch": [
        "data/*/dimension_type/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/dimension_type/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "worldgen/biome",
    "fileMatch": [
        "data/*/worldgen/biome/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/worldgen/biome/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "worldgen/noise_settings",
    "fileMatch": [
        "data/*/worldgen/noise_settings/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/worldgen/noise_settings/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "Loot Tables",
    "fileMatch": [
        "data/*/loot_tables/*/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/loot_tables/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "Animations",
    "fileMatch": [
        "assets/*/textures/*/*.mcmeta"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/animation/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "blockstates",
    "fileMatch": [
        "assets/*/blockstates/*/*.mcmeta"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/blockstates/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "font",
    "fileMatch": [
        "assets/*/font/*/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/font/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "pack",
    "fileMatch": [
        "assets/pack.mcmeta",
        "data/pack.mcmeta"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/pack/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "shaders_post",
    "fileMatch": [
        "assets/*/shaders_post/*/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/shaders_post/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "shaders_program",
    "fileMatch": [
        "assets/*/shaders_program/*/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/shaders_program/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "sounds",
    "fileMatch": [
        "assets/*/sounds.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/sounds/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "Item Models",
    "fileMatch": [
        "assets/*/models/item/*.json",
        "assets/*/models/items/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/item_models/schema.json"
},
{
    "name": "Java Edition Schema",
    "description": "Block Models",
    "fileMatch": [
        "assets/*/models/block/*.json",
        "assets/*/models/blocks/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/java-edition-schema/draft-01/block_models/schema.json"
}
```

### [shields.io](https://shields.io/)

```json
{
    "name": "Shields",
    "description": "A schema for https://shields.io/",
    "fileMatch": [
        "shields.io/*.json"
    ],
    "url": "https://legopitstop.github.io/JSON-Schemas/schemas/shields.io/schema.json"
}
```

### [Pack Update Schema](https://legopitstop.github.io/Update_Checker/)

```json
{
    "name": "Pack Update JSON",
    "description": "A schema for https://legopitstop.github.io/Update_Checker/update-checker.html",
    "fileMatch": [
        "update.json"
    ],
    "url": "https://legopitstop.github.io/Update_Checker/schema.json"
}
```

## UPDATES

Find the latest news about this schema via the [UPDATES](UPDATES.md) page

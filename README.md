# INFO

## [What are Schemas?](https://json-schema.org/understanding-json-schema/about.html)

Schemas are JSON files that will help and aid you in creating your code and
will show you any errors that will come up when loading up your mod. A good example
is the Minecraft Bedrock Addon Schemas. If you have that schema installed in VSC it will help
you by suggesting things to be added into the code. It also provides useful tooltips when you hover over the text to tell you what it does.

Join my discord to get live updates on schemas. [Discord](https://discord.gg/JbyTHWW)
<br>
[View Update Log](UPDATES.md)

## How to Install schemas for _Visual Studio Code_

1. Open VSC.
2. Go to your settings ( `CTRL` + `,` )
3. At the top corner you should find a button that will open settings (JSON). Click it.
4. Paste the below code into that JSON.
5. Save it. Thats it you're done!

```json
{
  "json.schemas": [
    // append json.schemas code here.
  ]
}
```

### Available Schemas

- [Minecraft: Bedrock Edition](./bedrock/README.md)
- [OptiFine](./optifine/README.md)
- [shields.io](./shields.io/README.md)
- [Spyglass](./spyglass/README.md)
- [Json Things](./jsonthings/README.md)

### [Pack Update Schema](https://legopitstop.github.io/Update_Checker/)

```json
{
  "name": "Pack Update JSON",
  "description": "A schema for https://legopitstop.github.io/Update_Checker/update-checker.html",
  "fileMatch": ["update.json"],
  "url": "https://raw.githubusercontent.com/legopitstop/Update_Checker/main/schema.json"
}
```

## UPDATES

Find the latest news about this schema via the [CHANGELOG](CHANGELOG.md) page

# Ideas

- Rewrite to use locale lang system.
  - Python script to create all languages
  - JSON that contains the translations `./lang/en_us.json`
  - The base schema contains the translation key. `{"test": {"description": "block.component.test"}}` -> `{"test": {"description": "This text has been translated"}}`
  - To use the translated schema use; `https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/schemas/:locale/bedrock/schema.json`
- bedrock/resource/ui - create "variable" def that will require any string that starts with `$` otherwise except the enum/number/bool

## TODO

- blocks.json

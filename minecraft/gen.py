import requests
import commentjson

tree = 'main' # preview or main
def vanilla_bedrock():
    with open('vanilla_bedrock.json', 'r') as fd:
        data = commentjson.load(fd)

    for url in ['mojang-biomes.json','mojang-blocks.json','mojang-camera-presets.json','mojang-cooldown-category.json','mojang-dimensions.json','mojang-effects.json','mojang-enchantments.json','mojang-entities.json','mojang-features.json','mojang-items.json',]:
        res = requests.get(f'https://github.com/Mojang/bedrock-samples/raw/{tree}/metadata/vanilladata_modules/'+url).json()
        minecraft_version = res['minecraft_version']
        vanilla_data_type = res['vanilla_data_type']
        data['definitions'][vanilla_data_type] = {"title": vanilla_data_type.title() + f' ({minecraft_version})', '$id': data['$id']+'#/definitions/'+vanilla_data_type, "$ref": "#/definitions/Identifier", 'examples': [item['name'] for item in res['data_items']]}

    # Material
    data['definitions']['materal'] = {
        "title": "Materal",
      "$id": "https://raw.githubusercontent.com/legopitstop/JSON-Schemas/main/minecraft/vanilla_bedrock.json#/definitions/materal",
      "type": "string",
      "examples": []
    }

    with open('src/entity.material') as fd:
        mat = commentjson.load(fd)
        for k, v in mat.get('materials').items():
            if k == 'version':
                data['definitions']['materal']['title'] += f' ({ v })'
            else:
                id = k.split(':')
                data['definitions']['materal']['examples'].append(id[0])

    with open('vanilla_bedrock.json', 'w') as fd:
        commentjson.dump(data, fd)

vanilla_bedrock()
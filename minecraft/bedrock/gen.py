import requests
import commentjson


def update(filename, url):
    print(filename)
    res = requests.get('https://github.com/Mojang/bedrock-samples/raw/main/metadata/vanilladata_modules/'+url).json()
    ver = res['minecraft_version']
    fp = 'minecraft/bedrock/'+filename
    with open(fp, 'r') as fd:
        data = commentjson.load(fd)
        data['title'] = res['vanilla_data_type'].title() + f' ({ver})'
        data['examples'] = [x['name'] for x in res['data_items']]

    with open(fp, 'w') as fd:
        commentjson.dump(data, fd)

# Biomes
update('biomes.json', 'mojang-biomes.json')
update('block.json', 'mojang-blocks.json')
update('camera_preset.json', 'mojang-camera-presets.json')
update('cooldown_category.json', 'mojang-cooldown-category.json')
update('dimension.json', 'mojang-dimensions.json')
update('mob_effect.json', 'mojang-effects.json')
update('enchantment.json', 'mojang-enchantments.json')
update('entity_type.json', 'mojang-entities.json')
update('feature.json', 'mojang-features.json')
update('item.json', 'mojang-items.json')
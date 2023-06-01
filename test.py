# Test all files in test/** and log any errors
# python test.py -all
# TODO
# - Add progressbar
import logging
import os
import sys
import glob
import json
import jsonschema
from jsonschema.exceptions import RefResolutionError
from progress.bar import IncrementalBar
import argparse
from multiprocessing import Pool

PATH = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(format='[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s', datefmt='%I:%M:%S',handlers=[logging.FileHandler(os.path.join(PATH, 'latest.log'),mode='w'),logging.StreamHandler(sys.stdout)], level=logging.INFO)

def fix(obj:dict):
    if isinstance(obj, dict):
        for key in obj:
            if key == '$ref':
                ref = obj['$ref']
                if ref.startswith('./'):
                    obj['$ref'] = 'file:///'+os.path.join(PATH, 'schemas', 'bedrock').replace(' ', '%20')+ref.replace('../', '/').replace('./', '/')
            else:
                fix(obj[key])
    elif isinstance(obj, list):
        for i in obj: fix(i)

def _path(*args):
    res = ''
    i=0
    for a in args:
        txt = ''
        if isinstance(a, str): txt=a
        elif isinstance(a, int): txt=f'[{a}]'
        if i==0: res+=txt
        else: res +='.'+txt
        i+=1

    return res

with open(os.path.join(PATH, 'schemas', 'bedrock', 'schema.json'), 'r') as r:
    try:
        SCHEMA = json.load(r)
        fix(SCHEMA)
    except json.decoder.JSONDecodeError as err:
        logging.error(f'Failed to load schema!: {err}')
        exit(1)

def test(name:str, instance:list):
    res = True
    
    bar = None
    if args.all is False:
        bar = IncrementalBar(name, max=len(instance))

    for fp in list(instance):
        if os.path.isfile(fp): # Only open if path is a file.
            with open(fp, 'r') as r:
                filename = fp.replace('\\', '/')
                try:
                    data = json.load(r)
                    jsonschema.validate(data, SCHEMA)
                    
                except RefResolutionError as err:
                    logging.error(f'{name} RefResolutionError: {err}')
                    exit(1)
                except jsonschema.SchemaError as err:
                    logging.error(f'{name} SchemaError: {err}')
                    exit(1)

                except (jsonschema.ValidationError) as err:
                    path = _path(*err.absolute_path)
                    logging.warning(f"{name} ValidationError '{filename}': {err.message} at {path}")
                    res = False

                except json.decoder.JSONDecodeError as err:
                    logging.error(f"{name} JSONDecodeError '{filename}': {err}")
                    res = False
        if bar is not None: bar.next()
    return res

parser = argparse.ArgumentParser(description='Arguments to test')

_args = ['all',
        'resoruce',
        'behavior',
        'ui',
        'flipbook_textures',
        'animations',
        'animation_controllers',
        'render_controllers',
        'client_entities',
        'attachables',
        'fogs',
        'entities',
        'items',
        'loot_tables',
        'recipes',
        'spawn_rules',
        'trading',
        'blocks',
        'models',
        "terrain_texture",
        "item_texture",
        'texture_set',
        'particles',
        'sound_definitions',
        'block_geometries',
        'features',
        'biomes',
        'feature_rules',
        'npc_dialogue',
        'spawn_groups',
        'volumes',
        'camera_entities',
        'font_metadata',
        'materials',
        'sounds',
        'cameras',
        'behavior_tree',
        'music_definitions',
        'pieces'
    ]

for arg in _args:
    parser.add_argument('-'+str(arg), nargs='?', const=True, default=False)
    
args = parser.parse_args()

# Resource Pack
def callback1():
    if args.all or args.resoruce or args.animation_controllers:
        files = glob.glob(PATH + '/tests/vanilla_RP/animation_controllers/**', recursive=True)
        if test('animation_controllers', files): logging.info('Animation Controllers: Passed')
        else: logging.warning('Animation Controllers: Failed')

def callback2():
    if args.all or args.resoruce or args.animations:
        files = glob.glob(PATH + '/tests/vanilla_RP/animations/**', recursive=True)
        if test('animations',files): logging.info('Animations: Passed')
        else: logging.warning('Animations: Failed')

def callback3():
    if args.all or args.resoruce or args.attachables:
        files = glob.glob(PATH + '/tests/vanilla_RP/attachables/**', recursive=True)
        if test('attachables',files): logging.info('Attachables: Passed')
        else: logging.warning('Attachables: Failed')

# TODO block geometry
def callback4():
    if args.all or args.behavior or args.block_geometries:
        print('block geometry')

# TODO blocks
def callback5():
    if args.all or args.behavior or args.blocks:
        print('blocks')

def callback6():
    if args.all or args.resoruce or args.client_entities:
        files = glob.glob(PATH + '/tests/vanilla_RP/entity/**', recursive=True)
        if test('client_entity',files): logging.info('Client Entity: Passed')
        else: logging.warning('Client Entity: Failed')
  
def callback7():
    if args.all or args.resoruce or args.flipbook_textures:
        if test('flipbook_textures',[os.path.join(PATH, 'tests', 'vanilla_RP', 'textures', 'flipbook_textures.json')]): logging.info('Flipbook Textures: Passed')
        else: logging.warning('Flipbook Textures: Failed')
    
def callback8():
    if args.all or args.resoruce or args.fogs:
        files = glob.glob(PATH + '/tests/vanilla_RP/fogs/**', recursive=True)
        if test('fogs',files): logging.info('Fogs: Passed')
        else: logging.warning('Fogs: Failed')

def callback9():
    if args.all or args.resoruce or args.models:
        files = glob.glob(PATH + '/tests/vanilla_RP/models/**', recursive=True)
        if test('models',files): logging.info('Models: Passed')
        else: logging.warning('Models: Failed')
 
# TODO particles
def callback10():
    if args.all or args.resoruce or args.particles:
        # files = glob.glob(PATH + '/tests/vanilla_RP/particles/**', recursive=True)
        # if test('particles',files): logging.info('Particles: Passed')
        # else: logging.warning('Particles: Failed')
        print('particles')

def callback11():
    if args.all or args.resoruce or args.render_controllers:
        files = glob.glob(PATH + '/tests/vanilla_RP/render_controllers/**', recursive=True)
        if test('render_controllers',files): logging.info('Render Controllers: Passed')
        else: logging.warning('Render Controllers: Failed')
        
def callback12():
    if args.all or args.resoruce or args.sound_definitions:
        if test('sound_definitions',[os.path.join(PATH, 'tests', 'vanilla_RP', 'sounds', 'sound_definitions.json')]): logging.info('Sound Definitions: Passed')
        else: logging.warning('Sound Definitions: Failed')
        
def callback13():
    if args.all or args.resoruce or args.terrain_texture:
        if test('terrain_texture',[os.path.join(PATH, 'tests', 'vanilla_RP', 'textures', 'terrain_texture.json')]): logging.info('Terrain Texture: Passed')
        else: logging.warning('Terrain Texture: Failed')
        
def callback14():
    if args.all or args.resoruce or args.item_texture:
        if test('item_texture',[os.path.join(PATH, 'tests', 'vanilla_RP', 'textures', 'item_texture.json')]): logging.info('Item Texture: Passed')
        else: logging.warning('Item Texture: Failed')
        
def callback15():
    if args.all or args.resoruce or args.texture_set:
        files = glob.glob(PATH + '/tests/vanilla_RTX/textures/**/*.texture_set.json', recursive=True)
        if test('texture_set',files): logging.info('Texture Set: Passed')
        else: logging.warning('Texture Set: Failed')
        
def callback16():
    if args.all or args.resoruce or args.ui:
        files = glob.glob(PATH + '/tests/vanilla_RP/ui/**', recursive=True)
        if test('ui',files): logging.info('UI: Passed')
        else: logging.warning('UI: Failed')
        
def callback17():
    if args.all or args.resoruce or args.camera_entities:
        files = glob.glob(PATH + '/tests/vanilla_RP/cameras/**', recursive=True)
        if test('cameras',files): logging.info('CAMERA_ENTITIES: Passed')
        else: logging.warning('CAMERA_ENTITIES: Failed')

def callback18():
    if args.all or args.resoruce or args.font_metadata:
        files = glob.glob(PATH + '/tests/vanilla_RP/font/font_metadata.json', recursive=True)
        if test('font_metadata',files): logging.info('FONT_METADATA: Passed')
        else: logging.warning('FONT_METADATA: Failed')

def callback19():
    if args.all or args.resoruce or args.materials:
        files = glob.glob(PATH + '/tests/vanilla_RP/materials/*.material', recursive=True)
        if test('materials',files): logging.info('MATERIALS: Passed')
        else: logging.warning('MATERIALS: Failed')

def callback20():
    if args.all or args.resoruce or args.sounds:
        files = glob.glob(PATH + '/tests/vanilla_RP/sounds.json', recursive=True)
        if test('sounds',files): logging.info('SOUNDS: Passed')
        else: logging.warning('SOUNDS: Failed')

def callback21():
    if args.all or args.resoruce or args.music_definitions:
        files = glob.glob(PATH + '/tests/vanilla_RP/sounds/music_definitions.json', recursive=True)
        if test('music_definitions',files): logging.info('MUSIC DEFINITATIONS: Passed')
        else: logging.warning('MUSIC DEFINITATIONS: Failed')

def callback22():
    if args.all or args.resoruce or args.pieces:
        files = glob.glob(PATH + '/tests/vanilla_RP/pieces/**/*.json', recursive=True)
        if test('pieces',files): logging.info('PIECES: Passed')
        else: logging.warning('PIECES: Failed')

# Behavior Pack

# TODO features
def callback30():
    if args.all or args.behavior or args.features:
        print('features')

# TODO biome
def callback31():
    if args.all or args.behavior or args.biomes:
        print('biome')

def callback32():
    if args.all or args.behavior or args.blocks:
        # files = glob.glob(PATH + '/tests/vanilla_BP/blocks/**', recursive=True)
        # if test('blocks',files): logging.info('Blocks: Passed')
        # else: logging.warning('Blocks: Failed')
        print('blocks')

def callback33():
    if args.all or args.behavior or args.entities:
        # files = glob.glob(PATH + '/tests/vanilla_BP/entities/**', recursive=True)
        # if test('entities',files): logging.info('Entity: Passed')
        # else: logging.warning('Entity: Failed')
        print('entities')

# TODO feature rules
def callback34():
    if args.all or args.behavior or args.feature_rules:
        print('feature rules')

def callback35():
    if args.all or args.behavior or args.items:
        files = glob.glob(PATH + '/tests/vanilla_BP/items/**', recursive=True)
        if test('items',files): logging.info('Items: Passed')
        else: logging.warning('Items: Failed')

def callback36():
    if args.all or args.behavior or args.loot_tables:
        files = glob.glob(PATH + '/tests/vanilla_BP/loot_tables/**', recursive=True)
        if test('loot_tables',files): logging.info('Loot Tables: Passed')
        else: logging.warning('Loot Tables: Failed')
        
# TODO npc dialogue
def callback37():
    if args.all or args.behavior or args.npc_dialogue:
        print('npc dialogue')

def callback38():
    if args.all or args.behavior or args.recipes:
        files = glob.glob(PATH + '/tests/vanilla_BP/recipes/**', recursive=True)
        if test('recipes',files): logging.info('Recipes: Passed')
        else: logging.warning('Recipes: Failed')
        
# TODO spawn groups
def callback39():
    if args.all or args.behavior or args.spawn_groups:
        print('spawn groups')

def callback40():
    if args.all or args.behavior or args.spawn_rules:
        # files = glob.glob(PATH + '/tests/vanilla_BP/spawn_rules/**', recursive=True)
        # if test('spawn_rules',files): logging.info('Spawn Rules: Passed')
        # else: logging.warning('Spawn Rules: Failed')
        print('spawn_rules')

def callback41():
    if args.all or args.behavior or args.trading:
        files = glob.glob(PATH + '/tests/vanilla_BP/trading/**', recursive=True)
        if test('trading',files): logging.info('Trading: Passed')
        else: logging.warning('Trading: Failed')
        
# TODO volume
def callback42():
    if args.all or args.behavior or args.volumes:
        print('volumes')

def callback43():
    if args.all or args.behavior or args.cameras:
        files = glob.glob(PATH + '/tests/vanilla_BP/cameras/**', recursive=True)
        if test('cameras',files): logging.info('CAMERAS: Passed')
        else: logging.warning('CAMERAS: Failed')

def callback44():
    if args.all or args.behavior or args.behavior_tree:
        files = glob.glob(PATH + '/tests/vanilla_BP/behavior_tree/**', recursive=True)
        if test('behavior_tree',files): logging.info('BEHAVIOR_TREE: Passed')
        else: logging.warning('BEHAVIOR_TREE: Failed')


def smap(f, *args):
    return f(*args)

def main():
    with Pool(30) as p:
        p.map(smap, [callback1,
                    callback2,
                    callback3,
                    callback4,
                    callback5,
                    callback6,
                    callback7,
                    callback8,
                    callback9,
                    callback10,
                    callback11,
                    callback12,
                    callback13,
                    callback14,
                    callback15,
                    callback16,
                    callback17,
                    callback18,
                    callback19,
                    callback20,
                    callback21,
                    callback22,

                    callback30,
                    callback31,
                    callback32,
                    callback33,
                    callback34,
                    callback35,
                    callback36,
                    callback37,
                    callback38,
                    callback39,
                    callback40,
                    callback41,
                    callback42,
                    callback43,
                    callback44,
                ])
    logging.info('DONE!!')

if __name__ == '__main__':
    main()
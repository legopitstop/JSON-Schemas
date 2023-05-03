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

    for fp in list(instance):
        if os.path.isfile(fp): # Only open if path is a file.
            with open(fp, 'r') as r:
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
                    logging.warning(f'{name} ValidationError "{fp}": {err.message} at {path}')
                    res = False

                except json.decoder.JSONDecodeError as err:
                    logging.error(f'{name} JSONDecodeError "{fp}": {err}')
                    res = False
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
        'sound_definitions'
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

# TODO blocks

def callback4():
    if args.all or args.resoruce or args.client_entities:
        files = glob.glob(PATH + '/tests/vanilla_RP/entity/**', recursive=True)
        if test('client_entity',files): logging.info('Client Entity: Passed')
        else: logging.warning('Client Entity: Failed')
  
def callback5():
    if args.all or args.resoruce or args.flipbook_textures:
        if test('flipbook_textures',[os.path.join(PATH, 'tests', 'vanilla_RP', 'textures', 'flipbook_textures.json')]): logging.info('Flipbook Textures: Passed')
        else: logging.warning('Flipbook Textures: Failed')
    
def callback6():
    if args.all or args.resoruce or args.fogs:
        files = glob.glob(PATH + '/tests/vanilla_RP/fogs/**', recursive=True)
        if test('fogs',files): logging.info('Fogs: Passed')
        else: logging.warning('Fogs: Failed')

def callback7():
    if args.all or args.resoruce or args.models:
        files = glob.glob(PATH + '/tests/vanilla_RP/models/**', recursive=True)
        if test('models',files): logging.info('Models: Passed')
        else: logging.warning('Models: Failed')
 
# if args.all or args.resoruce or args.particles:
#     files = glob.glob(PATH + '/tests/vanilla_RP/particles/**', recursive=True)
#     if test('particles',files): logging.info('Particles: Passed')
#     else: logging.warning('Particles: Failed')

def callback8():
    if args.all or args.resoruce or args.render_controllers:
        files = glob.glob(PATH + '/tests/vanilla_RP/render_controllers/**', recursive=True)
        if test('render_controllers',files): logging.info('Render Controllers: Passed')
        else: logging.warning('Render Controllers: Failed')
        
def callback9():
    if args.all or args.resoruce or args.sound_definitions:
        if test('sound_definitions',[os.path.join(PATH, 'tests', 'vanilla_RP', 'sounds', 'sound_definitions.json')]): logging.info('Sound Definitions: Passed')
        else: logging.warning('Sound Definitions: Failed')
        
def callback10():
    if args.all or args.resoruce or args.terrain_texture:
        if test('terrain_texture',[os.path.join(PATH, 'tests', 'vanilla_RP', 'textures', 'terrain_texture.json')]): logging.info('Terrain Texture: Passed')
        else: logging.warning('Terrain Texture: Failed')
        
def callback11():
    if args.all or args.resoruce or args.item_texture:
        if test('item_texture',[os.path.join(PATH, 'tests', 'vanilla_RP', 'textures', 'item_texture.json')]): logging.info('Item Texture: Passed')
        else: logging.warning('Item Texture: Failed')
        
def callback12():
    if args.all or args.resoruce or args.texture_set:
        files = glob.glob(PATH + '/tests/vanilla_RTX/textures/**/*.texture_set.json', recursive=True)
        if test('texture_set',files): logging.info('Texture Set: Passed')
        else: logging.warning('Texture Set: Failed')
        
def callback13():
    if args.all or args.resoruce or args.ui:
        files = glob.glob(PATH + '/tests/vanilla_RP/ui/**', recursive=True)
        if test('ui',files): logging.info('UI: Passed')
        else: logging.warning('UI: Failed')
        
# Behavior Pack

# TODO features

# TODO biome

# if args.all or args.behavior or args.blocks:
#     files = glob.glob(PATH + '/tests/vanilla_BP/blocks/**', recursive=True)
#     if test('blocks',files): logging.info('Blocks: Passed')
#     else: logging.warning('Blocks: Failed')

# if args.all or args.behavior or args.entities:
#     files = glob.glob(PATH + '/tests/vanilla_BP/entities/**', recursive=True)
#     if test('entities',files): logging.info('Entity: Passed')
#     else: logging.warning('Entity: Failed')

# TODO feature rules

def callback14():
    if args.all or args.behavior or args.items:
        files = glob.glob(PATH + '/tests/vanilla_BP/items/**', recursive=True)
        if test('items',files): logging.info('Items: Passed')
        else: logging.warning('Items: Failed')

def callback15():
    if args.all or args.behavior or args.loot_tables:
        files = glob.glob(PATH + '/tests/vanilla_BP/loot_tables/**', recursive=True)
        if test('loot_tables',files): logging.info('Loot Tables: Passed')
        else: logging.warning('Loot Tables: Failed')
        
# TODO npc dialogue

def callback16():
    if args.all or args.behavior or args.recipes:
        files = glob.glob(PATH + '/tests/vanilla_BP/recipes/**', recursive=True)
        if test('recipes',files): logging.info('Recipes: Passed')
        else: logging.warning('Recipes: Failed')
        
# TODO spawn groups

# if args.all or args.behavior or args.spawn_rules:
#     files = glob.glob(PATH + '/tests/vanilla_BP/spawn_rules/**', recursive=True)
#     if test('spawn_rules',files): logging.info('Spawn Rules: Passed')
#     else: logging.warning('Spawn Rules: Failed')

def callback17():
    if args.all or args.behavior or args.trading:
        files = glob.glob(PATH + '/tests/vanilla_BP/trading/**', recursive=True)
        if test('trading',files): logging.info('Trading: Passed')
        else: logging.warning('Trading: Failed')
        

# TODO volume
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
                    callback17
                ])
    logging.info('DONE!!')


if __name__ == '__main__':
    main()
# Test all files in test/** and log any errors
# python test.py -all
import logging
import os
import sys
import glob
import json
import jsonschema
from jsonschema.exceptions import RefResolutionError
import argparse

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
parser.add_argument('-all', nargs='?', const=True, default=False)
parser.add_argument('-resoruce', nargs='?', const=True, default=False)
parser.add_argument('-behavior', nargs='?', const=True, default=False)

parser.add_argument('-animations', nargs='?', const=True, default=False)
parser.add_argument('-animation_controllers', nargs='?', const=True, default=False)
parser.add_argument('-render_controllers', nargs='?', const=True, default=False)
parser.add_argument('-client_entities', nargs='?', const=True, default=False)
parser.add_argument('-attachables', nargs='?', const=True, default=False)
parser.add_argument('-fogs', nargs='?', const=True, default=False)
parser.add_argument('-entities', nargs='?', const=True, default=False)
parser.add_argument('-items', nargs='?', const=True, default=False)
parser.add_argument('-loot_tables', nargs='?', const=True, default=False)
parser.add_argument('-recipes', nargs='?', const=True, default=False)
parser.add_argument('-spawn_rules', nargs='?', const=True, default=False)
parser.add_argument('-trading', nargs='?', const=True, default=False)
parser.add_argument('-blocks', nargs='?', const=True, default=False)
parser.add_argument('-models', nargs='?', const=True, default=False)
args = parser.parse_args()

# Resource Pack

if args.all or args.resoruce or args.animations:
    files = glob.glob(PATH + '/tests/vanilla_RP/animations/**', recursive=True)
    if test('animations',files): logging.info('Animations: Passed')
    else: logging.warning('Animations: Failed')

if args.all or args.resoruce or args.animation_controllers:
    files = glob.glob(PATH + '/tests/vanilla_RP/animation_controllers/**', recursive=True)
    if test('animation_controllers', files): logging.info('Animation Controllers: Passed')
    else: logging.warning('Animation Controllers: Failed')

if args.all or args.resoruce or args.render_controllers:
    files = glob.glob(PATH + '/tests/vanilla_RP/render_controllers/**', recursive=True)
    if test('render_controllers',files): logging.info('Render Controllers: Passed')
    else: logging.warning('Render Controllers: Failed')

if args.all or args.resoruce or args.client_entities:
    files = glob.glob(PATH + '/tests/vanilla_RP/entity/**', recursive=True)
    if test('client_entity',files): logging.info('Client Entity: Passed')
    else: logging.warning('Client Entity: Failed')

if args.all or args.resoruce or args.attachables:
    files = glob.glob(PATH + '/tests/vanilla_RP/attachables/**', recursive=True)
    if test('attachables',files): logging.info('Attachables: Passed')
    else: logging.warning('Attachables: Failed')

if args.all or args.resoruce or args.fogs:
    files = glob.glob(PATH + '/tests/vanilla_RP/fogs/**', recursive=True)
    if test('fogs',files): logging.info('Fogs: Passed')
    else: logging.warning('Fogs: Failed')

if args.all or args.resoruce or args.models:
    files = glob.glob(PATH + '/tests/vanilla_RP/models/**', recursive=True)
    if test('models',files): logging.info('Models: Passed')
    else: logging.warning('Models: Failed')

# Behavior Pack

# if args.all or args.behavior or args.entities:
#     files = glob.glob(PATH + '/tests/vanilla_BP/entities/**', recursive=True)
#     if test('entities',files): logging.info('Entity: Passed')
#     else: logging.warning('Entity: Failed')

if args.all or args.behavior or args.items:
    files = glob.glob(PATH + '/tests/vanilla_BP/items/**', recursive=True)
    if test('items',files): logging.info('Items: Passed')
    else: logging.warning('Items: Failed')

if args.all or args.behavior or args.loot_tables:
    files = glob.glob(PATH + '/tests/vanilla_BP/loot_tables/**', recursive=True)
    if test('loot_tables',files): logging.info('Loot Tables: Passed')
    else: logging.warning('Loot Tables: Failed')

if args.all or args.behavior or args.recipes:
    files = glob.glob(PATH + '/tests/vanilla_BP/recipes/**', recursive=True)
    if test('recipes',files): logging.info('Recipes: Passed')
    else: logging.warning('Recipes: Failed')
    
# if args.all or args.behavior or args.blocks:
#     files = glob.glob(PATH + '/tests/vanilla_BP/blocks/**', recursive=True)
#     if test('blocks',files): logging.info('Blocks: Passed')
#     else: logging.warning('Blocks: Failed')

# if args.all or args.behavior or args.spawn_rules:
#     files = glob.glob(PATH + '/tests/vanilla_BP/spawn_rules/**', recursive=True)
#     if test('spawn_rules',files): logging.info('Spawn Rules: Passed')
#     else: logging.warning('Spawn Rules: Failed')

if args.all or args.behavior or args.trading:
    files = glob.glob(PATH + '/tests/vanilla_BP/trading/**', recursive=True)
    if test('trading',files): logging.info('Trading: Passed')
    else: logging.warning('Trading: Failed')

logging.info('DONE!!')
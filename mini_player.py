import zipfile
import os
import json

PACK_NAME = "mini_player.zip"
NAMESPACE = "mini"
VERSION = "1.21.4+"

def generate_datapack():
    mcmeta = {
        "pack": {
            "pack_format": 61,
            "description": f"Mini Player Scale Datapack for {VERSION}"
        }
    }

    shrink_cmd = (
        "# Shrink player to 1/5th size\n"
        "attribute @s minecraft:scale base set 0.2\n"
        "attribute @s minecraft:movement_speed base set 0.072\n"
        "attribute @s minecraft:jump_strength base set 0.28\n"
        "attribute @s minecraft:block_interaction_range base set 2.5\n"
        "attribute @s minecraft:entity_interaction_range base set 2.5\n"
        "attribute @s minecraft:step_height base set 0.4\n"
        "attribute @s minecraft:max_health base set 10\n"
        "attribute @s minecraft:gravity base set 0.04\n"
        "attribute @s minecraft:safe_fall_distance base set 12.0\n"
        "attribute @s minecraft:camera_distance base set 8"
    )

    reset_cmd = (
        "# Reset player to vanilla defaults\n"
        "attribute @s minecraft:scale base reset\n"
        "attribute @s minecraft:movement_speed base reset\n"
        "attribute @s minecraft:jump_strength base reset\n"
        "attribute @s minecraft:block_interaction_range base reset\n"
        "attribute @s minecraft:entity_interaction_range base reset\n"
        "attribute @s minecraft:step_height base reset\n"
        "attribute @s minecraft:max_health base reset\n"
        "attribute @s minecraft:gravity base reset\n"
        "attribute @s minecraft:safe_fall_distance base reset\n"
        "attribute @s minecraft:camera_distance base reset\n"
        "effect give @s minecraft:regeneration 1 255 true"
    )

    try:
        with zipfile.ZipFile(PACK_NAME, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('pack.mcmeta', json.dumps(mcmeta, indent=4))
            
            if os.path.exists("pack.png"):
                z.write("pack.png", "pack.png")
            else:
                print("Warning: logo not found in current directory.")

            z.writestr(f'data/{NAMESPACE}/function/shrink.mcfunction', shrink_cmd)
            z.writestr(f'data/{NAMESPACE}/function/reset.mcfunction', reset_cmd)
            
            load_msg = f'tellraw @a {{"text":"Mini Player Pack Loaded!","color":"green"}}'
            z.writestr(f'data/{NAMESPACE}/function/load.mcfunction', load_msg)
            
            load_tag = {"values": [f"{NAMESPACE}:load"]}
            z.writestr('data/minecraft/tags/function/load.json', json.dumps(load_tag))

        print(f"Successfully generated: {PACK_NAME}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_datapack()
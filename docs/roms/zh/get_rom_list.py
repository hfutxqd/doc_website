import os
import json


def is_odd(name):
    return name.endswith('.nes') or name.endswith('.NES')


nes_files = list(filter(is_odd, os.listdir('.')))
rom_list = {

}
PATH_PREFIX = '/roms/zh/'
for nes in nes_files:
    rom_list[nes[0:-4]] = {
        "name": nes[0:-4],
        "description": nes[0:-4],
        "url": PATH_PREFIX + nes
    }

print(json.dumps(rom_list, ensure_ascii=False))

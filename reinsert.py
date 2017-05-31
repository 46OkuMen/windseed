import os

#from rominfo import FILES, FILE_BLOCKS, CONTROL_CODES, POINTER_CONSTANT, EOF_CHAR
from romtools.disk import Disk, Gamefile, Block
from romtools.dump import DumpExcel, PointerExcel

ORIGINAL_ROM_PATH = os.path.join('original', 'Winds_Seed.FDI')
TARGET_ROM_PATH = os.path.join('patched', 'Winds_Seed.FDI')

OriginalWS = Disk(ORIGINAL_ROM_PATH)
TargetWS = Disk(TARGET_ROM_PATH)

FILES_TO_REINSERT = ['DRBIOS.COM', 'WS.COM']

for filename in FILES_TO_REINSERT:
    gamefile_path = os.path.join('original', filename)
    gamefile = Gamefile(gamefile_path, disk=OriginalWS, dest_disk=TargetWS)

    if filename == 'DRBIOS.COM':
        gamefile.edit(0x9c7, b'\x30\xE4\x2C\x40\xD0\xF8\x04\x40\x86\xE0\x66\x89\xC2\x90\x90\x90\x90\x90\x90\x90\x90\x90')   # halfwidth text
        gamefile.edit(0xa56, b'\x90\x90')  # nop out the cursor shl instruction
        gamefile.edit(0xa4d, b'\x90')  # make the text wrap at the end of the screen, not halfway through

    if filename == 'WS.COM':
        gamefile.edit(0x2532, b'\x0e')  # left window cursor
        gamefile.edit(0x25b5, b'\x40')  # right window cursor


        #gamefile.edit(0x5dfc, b'\x1c')  # start game cursor
        #gamefile.edit(0x5e0c, b'\x1c')  # start game cursor

        #gamefile.edit(0x5e00, b'Start Game')
        #gamefile.edit(0x5e10, b'Load Game ')

    """

        gamefile.edit(0x5e98, b'\x0e')  # 1st menu item cursor
        gamefile.edit(0x5ea4, b'\x0e')  # 2nd menu item cursor
        gamefile.edit(0x5eb0, b'\x0e')  # 3rd menu item cursor

        gamefile.edit(0x5f36, b'\x10')  # 2nd menu, 1st item cursor
        gamefile.edit(0x5f46, b'\x10')  # 2nd menu, 2nd item cursor
        gamefile.edit(0x5f56, b'\x10')  # 2nd menu, 3rd item cursor
        gamefile.edit(0x5f66, b'\x10')  # 2nd menu, 3rd item cursor

        gamefile.edit(0x6532, b'\x2c')  # left nametag?
        gamefile.edit(0x6360, b'\x2c')  # right nametag?

        gamefile.edit(0x6472, b'\x14')  # left nametag
        gamefile.edit(0x6481, b'\x16')  # right nametag?

        gamefile.edit(0x657a, b'\x1a')  # left nametag in status screen
        gamefile.edit(0x6584, b'\x1a')  # right nametag in status screen
        gamefile.edit(0x6592, b'\x26')  # status menu item
        gamefile.edit(0x65a1, b'\x26')  # status menu item
        gamefile.edit(0x65b0, b'\x26')  # status menu item
        gamefile.edit(0x65bf, b'\x26')  # status menu item
        gamefile.edit(0x65ce, b'\x1a')  # status menu item
        gamefile.edit(0x65e7, b'\x1a')  # status menu item

    """


    gamefile.write()

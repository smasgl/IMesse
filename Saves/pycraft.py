import os
import threading
import time
import math
from mcpi import block
from mcpi.minecraft import Minecraft


def restart_flat_world_script():
    os.system(f"cd ~ && python3 Documents/GitHub/IMesse/FlatWorldRestart.py")


def initialize(fileName):
    threading.Thread(target=restart_flat_world_script).start()
    time.sleep(6)
    global mc
    mc = Minecraft.create()
    mc.postToChat(f"Key: {fileName}")
    return mc, block

# WAND -------------------------------------------------------------------------------------

def wand_norden(x, y, z, hoehe, laenge, block):
    mc.setBlocks(x, y, z, x+laenge-1, y+hoehe-1, z, block)
    
def wand_osten(x, y, z, hoehe, laenge, block):
    mc.setBlocks(x, y, z, x, y+hoehe-1, z+laenge-1, block)
    
def wand_sueden(x, y, z, hoehe, laenge, block):
    mc.setBlocks(x, y, z, x-laenge+1, y+hoehe-1, z, block)
    
def wand_westen(x, y, z, hoehe, laenge, block):
    mc.setBlocks(x, y, z, x, y+hoehe-1, z-laenge+1, block)
    
def wand_norden_mit_fenster(x, y, z, hoehe, laenge, block):
    wand_norden(x, y, z, hoehe, laenge, block)
    if hoehe >= 3:
        mc.setBlocks(x+1, y+1, z, x+laenge-2, y+hoehe-2, z, 20)
    
def wand_osten_mit_fenster(x, y, z, hoehe, laenge, block):
    wand_osten(x, y, z, hoehe, laenge, block)
    if hoehe >= 3:
        mc.setBlocks(x, y+1, z+1, x, y+hoehe-2, z+laenge-2, 20)
    
def wand_sueden_mit_fenster(x, y, z, hoehe, laenge, block):
    wand_sueden(x, y, z, hoehe, laenge, block)
    if hoehe >= 3:
        mc.setBlocks(x-1, y+1, z, x-laenge+2, y+hoehe-2, z, 20)
    
def wand_westen_mit_fenster(x, y, z, hoehe, laenge, block):
    wand_westen(x, y, z, hoehe, laenge, block)
    if hoehe >= 3:
        mc.setBlocks(x, y+1, z-1, x, y+hoehe-2, z-laenge+2, 20)
    
def wand_rundum(x, y, z, hoehe, abstand, block):
    mc.setBlocks(x-abstand, y, z-abstand, x-abstand, y+hoehe-1, z+abstand, block)
    mc.setBlocks(x-abstand, y, z+abstand, x+abstand, y+hoehe-1, z+abstand, block)
    mc.setBlocks(x+abstand, y, z+abstand, x+abstand, y+hoehe-1, z-abstand, block)
    mc.setBlocks(x+abstand, y, z-abstand, x-abstand, y+hoehe-1, z-abstand, block)
        
def wand_rundum_mit_fenster(x, y, z, hoehe, abstand, block):
    wand_rundum(x, y, z, hoehe, abstand, block)
    if hoehe >= 3:
        mc.setBlocks(x-abstand, y+1, z-abstand+1, x-abstand, y+hoehe-2, z+abstand-1, 20)
        mc.setBlocks(x-abstand+1, y+1, z+abstand, x+abstand-1, y+hoehe-2, z+abstand, 20)
        mc.setBlocks(x+abstand, y+1, z+abstand-1, x+abstand, y+hoehe-2, z-abstand+1, 20)
        mc.setBlocks(x+abstand-1, y+1, z-abstand, x-abstand+1, y+hoehe-2, z-abstand, 20)

# BAUM -------------------------------------------------------------------------------------

def baum(x, y, z):
    mc.setBlocks(x, y, z, x, y+2, z, 17, 0)
    mc.setBlock(x, y+3, z, 18, 0)
    mc.setBlock(x+1, y+2, z, 18, 0)
    mc.setBlock(x-1, y+2, z, 18, 0)
    mc.setBlock(x, y+2, z+1, 18, 0)
    mc.setBlock(x, y+2, z-1, 18, 0)
    
# TÜRE -------------------------------------------------------------------------------------

def tuere_norden(x, y, z):
    mc.setBlock(x, y, z, 64, 0)
    mc.setBlock(x, y+1, z, 64, 8)
    
def tuere_osten(x, y, z):
    mc.setBlock(x, y, z, 64, 1)
    mc.setBlock(x, y+1, z, 64, 8)
    
def tuere_sueden(x, y, z):
    mc.setBlock(x, y, z, 64, 2)
    mc.setBlock(x, y+1, z, 64, 8)
    
def tuere_westen(x, y, z):
    mc.setBlock(x, y, z, 64, 3)
    mc.setBlock(x, y+1, z, 64, 8)
    
# BODEN -------------------------------------------------------------------------------------

def boden(x, y, z, laenge, breite, block):
    mc.setBlocks(x, y, z, x+laenge-1, y, z+breite-1, block)

def boden_rundum(x, y, z, abstand, block):
    mc.setBlocks(x-abstand, y, z-abstand, x+abstand-1, y, z+abstand-1, block)
    
# FENSTER -------------------------------------------------------------------------------------

def fenster_norden(x, y, z, hoehe, laenge):
    mc.setBlocks(x, y, z, x+laenge-1, y+hoehe-1, z, 20)
    
def fenster_osten(x, y, z, hoehe, laenge):
    mc.setBlocks(x, y, z, x, y+hoehe-1, z+laenge-1, 20)
    
def fenster_sueden(x, y, z, hoehe, laenge):
    mc.setBlocks(x, y, z, x-laenge+1, y+hoehe-1, z, 20)
    
def fenster_westen(x, y, z, hoehe, laenge):
    mc.setBlocks(x, y, z, x, y+hoehe-1, z-laenge+1, 20)

def fenster_rundum(x, y, z, hoehe, abstand):
    mc.setBlocks(x-abstand, y, z-abstand, x-abstand, y+hoehe-1, z+abstand, 20)
    mc.setBlocks(x-abstand, y, z+abstand, x+abstand, y+hoehe-1, z+abstand, 20)
    mc.setBlocks(x+abstand, y, z+abstand, x+abstand, y+hoehe-1, z-abstand, 20)
    mc.setBlocks(x+abstand, y, z-abstand, x-abstand, y+hoehe-1, z-abstand, 20)

# BLOCK -------------------------------------------------------------------------------------

def block_setzen(x, y, z, block, specific = 0):
    mc.setBlock(x, y, z, block, specific)
    
def bloecke_setzen(x, y, z, x2, y2, z2, block, specific = 0):
    mc.setBlocks(x, y, z, x2, y2, z2, block, specific)
    
# DACH -------------------------------------------------------------------------------------

def dach_rundum_der_spitze(x, y, z, hoehe, block):
    for i in range(hoehe):
        mc.setBlocks(x - i, y - i, z - i, x + i, y - i, z + i, block)
        
def dach(x, y, z, laenge, breite, block):
    if laenge > breite:
        max_counter = breite
    else:
        max_counter = laenge
    for i in range(math.ceil(max_counter/2)):
        mc.setBlocks(x + i, y + i, z + i, x + breite-1 - i, y + i, z + laenge-1 - i, block)
        
    

    

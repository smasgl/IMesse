import os, time, threading
def sub_func(): os.system(f"cd ~ && python3 Documents/GitHub/IMesse/FlatWorldRestart.py")
threading.Thread(target=sub_func).start()
time.sleep(6)
from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
mc.postToChat(f"Dies ist ein Beispiel Skript.")

#Beispiel Code
#Boden Bauen:
mc.setBlocks(-5, -1, -5, 5, -1, 5, block.WOOL.id)
#Linke Wand
mc.setBlocks(-5, -1, -5, -5, 2, 5, block.WOOD_PLANKS.id)
#Rechte Wand
mc.setBlocks(5, -1, -5, 5, 2, 5, block.WOOD_PLANKS.id)
#Vordere Wand
mc.setBlocks(-5, -1, -5, 5, 2, -5, block.WOOD_PLANKS.id)
#Hintere Wand
mc.setBlocks(-5, -1, 5, 5, 2, 5, block.WOOD_PLANKS.id)
#Türe
mc.setBlock(0, 0, -5, 64, 0)
mc.setBlock(0, 1, -5, 64, 8)
#Dach
for x in range(6):
    mc.setBlocks(0-x,8-x,0-x,0+x,8-x,0+x, 98, 0)
#Vordere Fenster
mc.setBlocks(-2,1,-5,-3,1,-5, block.GLASS.id)
mc.setBlocks(2,1,-5,3,1,-5, block.GLASS.id) 
#Linkes Fenster
mc.setBlocks(-5,1,3,-5,1,-3, block.GLASS.id)
#Rechtes Fenster
mc.setBlocks(5,1,3,5,1,-3, block.GLASS.id)
#Hinteres Fenster
mc.setBlocks(-3,1,5,3,1,5, block.GLASS.id) 



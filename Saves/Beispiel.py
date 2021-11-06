import pycraft
mc, block = pycraft.initialize(__file__[:-3])

#Mein Code
pycraft.wand_rundum_mit_fenster(0, 0, 0, 4, 5, block.WOOD_PLANKS.id)
pycraft.tuere_sueden(0, 0, 5)
pycraft.boden_rundum(0, -1, 0, 5, block.WOOL.id)
pycraft.dach_rundum_der_spitze(0,8,0,6,block.COBBLESTONE.id)
pycraft.baum(-3, 0, 8)
pycraft.baum(3, 0, 8)

mc.setBlocks(1, 0, 1, 3, 2, 3, block.TNT.id, 1)
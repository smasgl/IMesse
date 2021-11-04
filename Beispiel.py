import pycraft
mc, block = pycraft.initialize(__file__[:-3])

#pycraft.wand_vorne(0, 0, 0, 3, 5, block.WOOL.id)
#pycraft.wand_seite(0, 0, 0, 3, 5, block.WOOL.id)
#pycraft.baum(0, 0, 0)
#pycraft.wand_rundum_mit_fenster(0, 0, 0, 4, 5, block.WOOD_PLANKS.id)
#pycraft.baum(2, 0, 0)
#pycraft.tuere_norden(0, 0, 5)

#pycraft.wand_norden_mit_fenster(0, 0, 0, 3, 5, block.WOOL.id)
#pycraft.wand_osten_mit_fenster(0, 0, 0, 3, 5, block.WOOD_PLANKS.id)
#pycraft.wand_sueden_mit_fenster(0, 0, 0, 3, 5, block.WOOL.id)
#pycraft.wand_westen_mit_fenster(0, 0, 0, 3, 5, block.WOOD_PLANKS.id)

#pycraft.boden(0, 0, 0, 4,4, block.WOOD_PLANKS.id)

#pycraft.(0,0,0,0,5,0, 1)

#pycraft.dach_rundum_der_spitze(0,10,0,5,1)

pycraft.dach(0,0,0,60,60,1)

#pycraft.fenster_norden(0, 0, 0, 1, 1)

# # Beispiel Code
# # Boden Bauen:
# mc.setBlocks(-5, -1, -5, 5, -1, 5, block.WOOL.id)
# # Linke Wand
# mc.setBlocks(-5, -1, -5, -5, 2, 5, block.WOOD_PLANKS.id)
# # Rechte Wand
# mc.setBlocks(5, -1, -5, 5, 2, 5, block.WOOD_PLANKS.id)
# # Vordere Wand
# mc.setBlocks(-5, -1, -5, 5, 2, -5, block.WOOD_PLANKS.id)
# # Hintere Wand
# mc.setBlocks(-5, -1, 5, 5, 2, 5, block.WOOD_PLANKS.id)
# # Türe
# mc.setBlock(0, 0, -5, 64, 0)
# mc.setBlock(0, 1, -5, 64, 8)
# # Dach
# for x in range(6):
#     mc.setBlocks(0 - x, 8 - x, 0 - x, 0 + x, 8 - x, 0 + x, 98, 0)
# # Vordere Fenster
# mc.setBlocks(-2, 1, -5, -3, 1, -5, block.GLASS.id)
# mc.setBlocks(2, 1, -5, 3, 1, -5, block.GLASS.id)
# # Linkes Fenster
# mc.setBlocks(-5, 1, 3, -5, 1, -3, block.GLASS.id)
# # Rechtes Fenster
# mc.setBlocks(5, 1, 3, 5, 1, -3, block.GLASS.id)
# # Hinteres Fenster
# mc.setBlocks(-3, 1, 5, 3, 1, 5, block.GLASS.id)

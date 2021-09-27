from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc = Minecraft.create()
mc.player.setPos(0, 50, 0)
pos = mc.player.getPos()
    
def ClearArea(size):
    mc.setBlocks(pos.x-size, pos.y-size, pos.z-size, pos.x+size, pos.y+size, pos.z+size, 0)
    
def GenerateLogo(delay, firstBack, firstFront, lastBack, lastFront):
    time.sleep(delay)
    DrawBackground(firstBack)
    time.sleep(delay)
    DrawL(firstFront)
    time.sleep(delay)
    DrawI(firstFront)
    time.sleep(delay)
    DrawE(firstFront)
    time.sleep(delay)
    DrawB(firstFront)
    time.sleep(delay)
    DrawH(firstFront)
    time.sleep(delay)
    DrawE2(firstFront)
    time.sleep(delay)
    DrawR(firstFront)
    time.sleep(delay)
    DrawR2(firstFront)
    time.sleep(delay)
    DrawBackground(lastBack)
    DrawL(lastFront)
    DrawI(lastFront)
    DrawE(lastFront)
    DrawB(lastFront)
    DrawH(lastFront)
    DrawE2(lastFront)
    DrawR(lastFront)
    DrawR2(lastFront)


def DrawBackground(blockType):
    mc.setBlocks(pos.x-19, pos.y+1, pos.z+30, pos.x+19, pos.y+9, pos.z+31, blockType)
    mc.setBlocks(pos.x-18, pos.y+2, pos.z+30, pos.x+18, pos.y+8, pos.z+30, 0)

def DrawL(blockType):
    mc.setBlocks(17, 57, 30, 16, 53, 30, blockType)
    mc.setBlocks(15, 53, 30, 15, 54, 30, blockType)
    
def DrawI(blockType):
    mc.setBlocks(13, 57, 30, 12, 53, 30, blockType)
    
def DrawE(blockType):
    mc.setBlocks(10, 57, 30, 9, 53, 30, blockType)
    mc.setBlock(8, 57, 30, blockType)
    mc.setBlock(8, 55, 30, blockType)
    mc.setBlock(8, 53, 30, blockType)
    
def DrawB(blockType):
    mc.setBlocks(6, 57, 30, 5, 53, 30, blockType)
    mc.setBlock(4, 57, 30, blockType)
    mc.setBlock(4, 55, 30, blockType)
    mc.setBlock(4, 53, 30, blockType)
    mc.setBlock(3, 56, 30, blockType)
    mc.setBlock(3, 54, 30, blockType)
    
def DrawH(blockType):
    mc.setBlocks(1, 57, 30, 0, 53, 30, blockType)
    mc.setBlocks(-2, 57, 30, -3, 53, 30, blockType)
    mc.setBlock(-1, 55, 30, blockType)
    
def DrawE2(blockType):
    mc.setBlocks(-5, 57, 30, -6, 53, 30, blockType)
    mc.setBlock(-7, 57, 30, blockType)
    mc.setBlock(-7, 55, 30, blockType)
    mc.setBlock(-7, 53, 30, blockType)
    
def DrawR(blockType):
    mc.setBlocks(-10, 57, 30, -9, 53, 30, blockType)
    mc.setBlock(-11, 57, 30, blockType)
    mc.setBlock(-11, 54, 30, blockType)
    mc.setBlock(-12, 53, 30, blockType)
    mc.setBlock(-12, 56, 30, blockType)
    mc.setBlock(-12, 55, 30, blockType)
    
def DrawR2(blockType):
    mc.setBlocks(-15, 57, 30, -14, 53, 30, blockType)
    mc.setBlock(-16, 57, 30, blockType)
    mc.setBlock(-16, 54, 30, blockType)
    mc.setBlock(-17, 53, 30, blockType)
    mc.setBlock(-17, 56, 30, blockType)
    mc.setBlock(-17, 55, 30, blockType)

def ClearBuildingArea():
    mc.setBlocks(pos.x-8, pos.y, pos.z-2, pos.x+8, pos.y+50, pos.z+15, 0)
  
def GenerateBuildingAreaOuterRing(blockType):
    mc.setBlocks(pos.x-8, pos.y-1, pos.z-2, pos.x+8, pos.y-1, pos.z+15, blockType)
    
def GenerateBuildingAreaOuterFence():
    mc.setBlocks(pos.x-8, pos.y, pos.z-2, pos.x-8, pos.y, pos.z+15, block.FENCE)
    mc.setBlocks(pos.x+8, pos.y, pos.z-2, pos.x+8, pos.y, pos.z+15, block.FENCE)
    mc.setBlocks(pos.x-8, pos.y, pos.z-2, pos.x+8, pos.y, pos.z-2, block.FENCE)
    mc.setBlocks(pos.x-8, pos.y, pos.z+15, pos.x+8, pos.y, pos.z+15, block.FENCE)
    
def GenerateBuildingAreaInnerGround(blockType):
    mc.setBlocks(pos.x-5, pos.y-1, pos.z+2, pos.x+5, pos.y-1, pos.z+12, blockType)

def GenerateBuildingAreaPositionBlock(blockType):
    mc.setBlock(pos.x, pos.y-1, pos.z, blockType)
    
def GenerateBuildingAreaMarkers():
    mc.setBlock(pos.x-5, pos.y+11, pos.z+2, block.WOOL.id, 2)
    mc.setBlock(pos.x+5, pos.y+11, pos.z+2, block.WOOL.id, 2)
    mc.setBlock(pos.x-5, pos.y+11, pos.z+12, block.WOOL.id, 2)
    mc.setBlock(pos.x+5, pos.y+11, pos.z+12, block.WOOL.id, 2)
    mc.setBlock(pos.x-5, pos.y-1, pos.z+2, block.WOOL.id, 2)
    mc.setBlock(pos.x+5, pos.y-1, pos.z+2, block.WOOL.id, 2)
    mc.setBlock(pos.x-5, pos.y-1, pos.z+12, block.WOOL.id, 2)
    mc.setBlock(pos.x+5, pos.y-1, pos.z+12, block.WOOL.id, 2)

def GenerateBuildingArea():
    ClearBuildingArea()
    GenerateBuildingAreaOuterRing(block.CLAY.id)
    GenerateBuildingAreaPositionBlock(block.DIAMOND_BLOCK.id)
    GenerateBuildingAreaOuterFence()
    GenerateBuildingAreaInnerGround(block.GRASS)
    GenerateBuildingAreaMarkers()
    
def GenerateArea():
    ClearArea(50)
    GenerateBuildingArea()
    time.sleep(3)
    GenerateLogo(0.5, 3, 1, 7, 41)
    
GenerateArea()
    
    

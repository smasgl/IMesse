import os
import threading
import time
from mcpi import block
from mcpi.minecraft import Minecraft


def restart_flat_world_script():
    os.system(f"cd ~ && python3 Documents/GitHub/IMesse/FlatWorldRestart.py")


def initialize():
    threading.Thread(target=restart_flat_world_script).start()
    time.sleep(6)
    mc = Minecraft.create()
    mc.postToChat(f"Dies ist ein Beispiel Skript.")
    return mc, block;



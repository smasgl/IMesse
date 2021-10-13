import os, time, threading
def sub_func(): os.system(f"cd ~ && python3 Documents/GitHub/IMesse/FlatWorldRestart.py")
threading.Thread(target=sub_func).start()
time.sleep(6)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat(f"Key: {os.path.basename(__file__)[:4]}")

#Dein Code

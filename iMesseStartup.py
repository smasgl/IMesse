#!/usr/bin/env python

import os
from random import randint

saves = r'/home/pi/Documents/GitHub/IMesse/Saves'
iMesse = r'/home/pi/Documents/GitHub/IMesse'

os.system(f"rm {iMesse}/SavesLastProject.py")
randomKey = randint(1000, 9999)
while os.path.exists(f"{randomKey}.py"):
    randomKey = randint(1000, 9999)
f = open(f"{saves}/{randomKey}.py", "w")
f.write("import os, time, threading\n")
f.write(f'def sub_func(): os.system(f"cd ~ && python3 Documents/GitHub/IMesse/FlatWorldRestart.py")\n')
f.write(f'threading.Thread(target=sub_func).start()\n')
f.write("time.sleep(5)\n")
f.write(f'from mcpi.minecraft import Minecraft\n')
f.write(f'mc = Minecraft.create()\n')
f.write('mc.postToChat(f"Key: {os.path.basename(__file__)[:4]}")\n\n')
f.close()
f = open(f"{iMesse}/SavesLastProject.py", "w")
f.write("import os\n")
f.write(f'os.system(f"thonny {saves}/{randomKey}.py")')
f.close()
os.system(f"python3 {iMesse}/SavesLastProject.py")
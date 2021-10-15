#!/usr/bin/env python

import os, time
from random import randint

saves = r'/home/pi/Documents/GitHub/IMesse/Saves'
iMesse = r'/home/pi/Documents/GitHub/IMesse'
windowScript = r'/home/pi/Documents/GitHub/IMesse/CloseThonnyWindows.py'

os.system(f"rm {iMesse}/SavesLastProject.py")
randomKey = randint(1000, 9999)
while os.path.exists(f"{randomKey}.py"):
    randomKey = randint(1000, 9999)
os.system(f"mkdir {saves}")
f = open(f"{saves}/{randomKey}.py", "w")
f.write("import os, time, threading\n")
f.write(f'def sub_func(): os.system(f"cd ~ && python3 Documents/GitHub/IMesse/FlatWorldRestart.py")\n')
f.write(f'threading.Thread(target=sub_func).start()\n')
f.write("time.sleep(6)\n")
f.write(f'from mcpi.minecraft import Minecraft\n')
f.write(f'from mcpi import block\n')
f.write(f'mc = Minecraft.create()\n')
f.write('mc.postToChat(f"Key: {os.path.basename(__file__)[:4]}")\n\n')
f.write('#Dein Code\n')
f.close()
f = open(f"{iMesse}/SavesLastProject.py", "w")
f.write("import os, time, threading\n")
f.write(f'def window_func(): os.system(f"cd ~ && python3 {windowScript}")\n')
f.write(f'def beispiel_func(): os.system(f"thonny {iMesse}/Beispiel.py")\n')
f.write(f'def saves_func(): os.system(f"thonny {saves}/{randomKey}.py")\n')
f.write(f'threading.Thread(target=window_func).start()\n')
f.write(f'threading.Thread(target=beispiel_func).start()\n')
f.write(f'time.sleep(1)\n')
f.write(f'threading.Thread(target=saves_func).start()\n')
f.close()
os.system(f"python3 {iMesse}/SavesLastProject.py")
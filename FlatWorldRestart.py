#!/usr/bin/env python

import os
import sys
import shutil
from pynput.keyboard import Key, Controller, Listener
import time
from distutils.dir_util import copy_tree

world = r'/home/pi/Documents/GitHub/IMesse/FlatWorld'
folder = r'/home/pi/.minecraft/games/com.mojang/minecraftWorlds'
desktop = r'/usr/share/raspi-ui-overrides/applications/minecraft-pi.desktop'
windowScript = r'/home/pi/Documents/GitHub/IMesse/CloseWindows.py'

def on_press(key):
    keyboard = Controller()
    if key == Key.esc:
        os.system(f"python3 {windowScript}")
        return False
    
def execute_script():
    keyboard = Controller()
    os.system(f"python3 {windowScript}")
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    copy_tree(world, folder)
    os.system(f"xdg-open {desktop}")
    time.sleep(0.4)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.alt)
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)
    keyboard.release(Key.alt)

    with Listener(
            on_press=on_press) as listener:
        listener.join()

execute_script()
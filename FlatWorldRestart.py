#!/usr/bin/env python

import os
import sys
import shutil
from pynput.keyboard import Key, Controller, Listener
import time
from distutils.dir_util import copy_tree
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

world = r'/home/pi/Documents/GitHub/IMesse/FlatWorld'
folder = r'/home/pi/.minecraft/games/com.mojang/minecraftWorlds'
desktop = r'/usr/share/raspi-ui-overrides/applications/minecraft-pi.desktop'
windowScript = r'/home/pi/Documents/GitHub/IMesse/CloseWindows.py'
    
keyboard = Controller()
os.system(f"python3 {windowScript}")
os.system(f"xdg-open {desktop}")
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
time.sleep(0.7)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
screen = Wnck.Screen.get_default()
screen.force_update()
windows = screen.get_windows()
for w in windows:
    if 'Minecraft' in w.get_name():
        w.maximize()
        break
    

#!/usr/bin/env python

import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
screen = Wnck.Screen.get_default()
screen.force_update()
windows = screen.get_windows()
for w in windows:
    if 'Thonny' in w.get_name():
        w.close(0)
import os, time, threading
def window_func(): os.system(f"cd ~ && python3 /home/pi/Documents/GitHub/IMesse/CloseThonnyWindows.py")
def beispiel_func(): os.system(f"thonny /home/pi/Documents/GitHub/IMesse/Saves/Beispiel.py")
def saves_func(): os.system(f"thonny /home/pi/Documents/GitHub/IMesse/Saves/3467.py")
threading.Thread(target=window_func).start()
threading.Thread(target=beispiel_func).start()
time.sleep(1)
threading.Thread(target=saves_func).start()

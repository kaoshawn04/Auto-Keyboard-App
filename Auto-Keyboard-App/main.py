import os
import sys
import time
import pyuac
import keyboard

#try:
from library.common.action import Keyboard
from library.windows.api import Windows_api

# except (ImportError, ModuleNotFoundError):
#     dir_path = (os.path.realpath(__file__)).rsplit("\\library", 1)[0]
#     sys.path.append(dir_path)
# 
#     from library.common.action import Keyboard
#     from library.windows.api import Windows_api
    
    
def press_key(key):
    Windows_api.block_input(True)
    
    Keyboard.keydown("0")
    time.sleep(0.7)
    Keyboard.keyup("0")

    Windows_api.block_input(False)
    
    
def main():
    while True:
        if keyboard.is_pressed("x"):
            break
        
        press_key("0")
        time.sleep(180)
        

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()

    else:
        window = Windows_api.find_window(window_name="MapleStory Worlds-Artale (繁體中文版)")
        Windows_api.set_foreground_window(window)
        
        main()
        
# test
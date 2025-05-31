import os
import sys
import time
import pyuac
import keyboard

from library.common.action import Keyboard
from library.windows.api import Windows_api


def press_key(key):
    Windows_api.block_input(True)
    time.sleep(0.2)
    Windows_api.remove_message()
    Windows_api.block_input(False)
    
    Keyboard.keydown("0")
    time.sleep(1)
    Keyboard.keyup("0")

    
def main():
    while True:
        if keyboard.is_pressed("x"):
            break
        
        press_key("0")
        time.sleep(180)
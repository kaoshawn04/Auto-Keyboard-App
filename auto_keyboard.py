import json
import time
import threading

from library.common.path import realpath
from library.common.action import Keyboard
from library.windows.api import Windows_api


class AutoKeyboard:
    def __init__(self):
        self.threads = []
        self.running = False
            
        
    def press_key(self, key, interval, repeat):
        if repeat[1] == 0:
            count = float("inf")
            
        else:
            count = repeat[0]
            
        while count > 0 and self.running == True:
            Windows_api.block_input(True)
            Windows_api.remove_message()
            Windows_api.block_input(False)

            Keyboard.press(key, interval=0.5)
            
            time.sleep(float(interval))
            
            count -= 1
            
            
    def run(self):
        keysets = json.load(open(realpath("keysets.json"), "r"))
        
        window = Windows_api.find_window(window_name="MapleStory Worlds-Artale (繁體中文版)")
        if window is not None:
            Windows_api.set_foreground_window(window)
        
        for keyset in keysets:
            t = threading.Thread(
                target=self.press_key, 
                args=(keyset["key"], keyset["interval"], keyset["repeat"]),
                daemon=True
            )
            t.start()
            self.threads.append(t)


    def start(self):
        if not self.running:
            self.running = True
            self.threads = []
            self.run()


    def stop(self):
        if self.running:
            self.running = False
            self.threads = []
import time
from .main import Song
import os


class WakeUp(object):
    def __init__(self):
        os.chdir(os.path.dirname(__file__))
        self.s = Song(r'./test-music/weakup.mp3')
        self.s.volume(0)
        while True:
            self.s.play()
            time.sleep(1)
            self.s.stop()
            time.sleep(100)

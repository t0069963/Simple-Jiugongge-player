import os

if os.name != 'nt':
    raise Exception("can't run on this system.")


def load(filename):
    from .main import Song
    return Song(filename)


def loadlist(path):
    from .songlist import SongList
    return SongList(path)


def wakeup():
    from .wakeup import WakeUp
    WakeUp()

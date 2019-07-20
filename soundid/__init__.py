import glob
from tinytag import TinyTag

from .version import __version__


class Sound:

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    @property
    def name(self):
        return '{} - {}'.format(self.artist, self.title)
    

class Database:

    def __init__(self, filename, soundpaths=None):
        self.filename = filename
        self._sounds = []
        
        for soundpath in soundpaths:
            for soundfile in glob.glob(soundpath):
                tag = TinyTag.get(soundfile)
                self._sounds.append(Sound(tag.artist, tag.title))

    @property
    def sounds(self):
        return self._sounds

    @property
    def number_of_sounds(self):
        return len(self._sounds)

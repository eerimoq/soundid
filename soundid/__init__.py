import glob
from tinytag import TinyTag
from skimage.feature import peak_local_max
from pydub import AudioSegment
import matplotlib.mlab as mlab
import matplotlib.pyplot as plot

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
        """A list of all sounds in the database.

        """
        
        return self._sounds

    @property
    def number_of_sounds(self):
        """Number of sounds in the database.

        """
        
        return len(self._sounds)

    def identify_file(self, soundfile):
        """Identify given sound file.

        Returns the identified sound, or ``None`` if the sound was not
        identified.

        """

        sound = AudioSegment.from_file(soundfile)
        samples = sound.get_array_of_samples()
        fingerprint = create_fingerprint(samples[0::sound.channels],
                                         sound.frame_rate)

        return self._sounds[0]


def create_fingerprint(samples, sampling_rate):
    """Create a fingerprint of given samples.

    """

    spectrum, freqs, times = mlab.specgram(samples,
                                           NFFT=4096,
                                           Fs=sampling_rate,
                                           window=mlab.window_hanning,
                                           noverlap=2048)
    coordinates = peak_local_max(spectrum, min_distance=5)

    plot.specgram(samples,
                  NFFT=4096,
                  Fs=sampling_rate,
                  window=mlab.window_hanning,
                  noverlap=2048)
    plot.xlabel('Time')
    plot.ylabel('Frequency')
    plot.show()   

    fingerprint = []
    
    for x, y in coordinates:
        fingerprint.append((int(1000 * times[y]), int(freqs[x])))

    for t, f in sorted(fingerprint):
        print(t, f)

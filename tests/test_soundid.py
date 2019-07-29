import unittest
import soundid


class DatabaseTest(unittest.TestCase):

    def test_create_database(self):
        database = soundid.Database('test_create_database.sid',
                                    [
                                        'tests/files/foo.mp3',
                                        'tests/files/bar.mp3'
                                    ])
        self.assertEqual(database.number_of_sounds, 2)
        self.assertEqual(database.sounds[0].artist, 'Foo Band')
        self.assertEqual(database.sounds[0].title, 'Foo Song')
        self.assertEqual(database.sounds[0].name, 'Foo Band - Foo Song')
        self.assertEqual(database.sounds[1].name, 'Bar Artist - Bar Song')

    def test_identify_file(self):
        database = soundid.Database('test_identify_file.sid',
                                    ['tests/files/foo.mp3'])
        sound = database.identify_file('tests/files/foo.mp3')
        self.assertEqual(sound.title, 'Foo Song')

    def test_identify_file_sine_440hz(self):
        database = soundid.Database('test_identify_file.sid',
                                    ['tests/files/sine-440hz.mp3'])
        sound = database.identify_file('tests/files/sine-440hz.mp3')
        self.assertEqual(sound.title, '')


if __name__ == '__main__':
    unittest.main()

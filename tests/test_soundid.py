import unittest
import soundid


class SoundIdTest(unittest.TestCase):

    def test_create_database(self):
        database = soundid.Database('test_create_database.sid',
                                    [
                                        'tests/files/foo.mp3',
                                        'tests/files/bar.mp3'
                                    ])
        self.assertEqual(database.number_of_sounds, 2)
        self.assertEqual(database.sounds[0].name, 'Foo Band - Foo Song')
        self.assertEqual(database.sounds[1].name, 'Bar Artist - Bar Song')


if __name__ == '__main__':
    unittest.main()

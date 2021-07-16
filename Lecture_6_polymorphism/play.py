def start_playing(obj):
    return obj.play()


import unittest


class PlayingTest(unittest.TestCase):
    def test(self):
        class Test:
            def play(self):
                return "test"

        res = start_playing(Test())
        self.assertEqual(res, "test")


if __name__ == '__main__':
    unittest.main()


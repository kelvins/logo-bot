import sys
import unittest
import os
import time

sys.path.append('./src')
from logo import Logo
from logobot import LogoBot


class LogoBotTest(unittest.TestCase):

    def test_run(self):
        path = os.path.dirname(os.path.abspath(__file__))
        output_path = path + "/../output/"
        logo = Logo(path + "/../input/", path + "/../logo.png", output_path, 20, "bottom_right", "png")
        logo_bot = LogoBot(logo)

        for dirname, dirnames, filenames in os.walk(output_path):
            for filename in filenames:
                try:
                    os.remove(dirname+filename)
                except Exception:
                    pass

        self.assertEqual(len(os.listdir(output_path)), 0)

        logo_bot.start()
        time.sleep(5)
        self.assertEqual(len(os.listdir(output_path)), 3)
        logo_bot.stop()

if __name__ == '__main__':
    unittest.main()

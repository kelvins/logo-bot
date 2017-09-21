import sys
import unittest
import os
import StringIO
import time

sys.path.append('./src')
from logo import Logo
import logobot


class LogoBotTest(unittest.TestCase):

    @staticmethod
    def clear_dir(path):
        for dir_name, dir_names, file_names in os.walk(path):
            for file_name in file_names:
                try:
                    os.remove(dir_name + file_name)
                except Exception:
                    pass

    def test_run(self):
        path = os.path.dirname(os.path.abspath(__file__))
        output_path = path + "/../output/"
        logo = Logo(path + "/../input/", path + "/../logo.png", output_path, 20, "bottom_right", "png")
        logo_bot = logobot.LogoBot(logo)

        self.clear_dir(output_path)

        self.assertEqual(len(os.listdir(output_path)), 0)

        logo_bot.start()
        time.sleep(5)
        self.assertEqual(len(os.listdir(output_path)), 3)
        logo_bot.stop()

    def test_args(self):
        path = os.path.dirname(os.path.abspath(__file__))
        input_path = path + "/../input/"
        logo_path = path + "/../logo.png"
        output_path = path + "/../output/"
        size = "20"
        position = "bottom_right"
        type = "png"

        self.clear_dir(output_path)

        self.assertEqual(len(os.listdir(output_path)), 0)

        # Simulates the user input (raw_input)
        quit_command = StringIO.StringIO("q")
        sys.stdin = quit_command

        logobot.main(["-i", input_path, "-l", logo_path, "-o", output_path, "-s", size, "-p", position, "-t", type])
        
        # Wait some seconds until the images are saved
        time.sleep(5)
        
        self.assertEqual(len(os.listdir(output_path)), 3)

if __name__ == '__main__':
    unittest.main()

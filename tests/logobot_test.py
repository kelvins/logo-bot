import sys
import unittest
import os
import StringIO
import time
import shutil

sys.path.append('./src')
from logo import Logo
import logobot


class LogoBotTest(unittest.TestCase):

    path = os.path.dirname(os.path.abspath(__file__))
    input_path = path + "/../input/"
    output_path = path + "/../output/"
    logo_path = path + "/../logo.png"

    @staticmethod
    def clear_dir(path):
        for dir_name, dir_names, file_names in os.walk(path):
            for file_name in file_names:
                try:
                    os.remove(dir_name + file_name)
                except Exception:
                    pass

    def test_run(self):
        logo = Logo(self.input_path, self.logo_path, self.output_path, 20, "bottom_right", "png")
        logo_bot = logobot.LogoBot(logo)

        self.clear_dir(self.output_path)

        self.assertEqual(len(os.listdir(self.output_path)), 0)

        logo_bot.start()

        time.sleep(5)
        self.assertEqual(len(os.listdir(self.output_path)), 3)

        shutil.copy(self.logo_path, self.input_path + "logo.png")
        
        time.sleep(2)
        self.assertEqual(len(os.listdir(self.output_path)), 4)

        logo_bot.stop()

        os.remove(self.input_path + "logo.png")
        self.assertEqual(len(os.listdir(self.input_path)), 3)

    def test_args(self):
        size = "20"
        position = "bottom_right"
        type = "png"

        self.clear_dir(self.output_path)

        self.assertEqual(len(os.listdir(self.output_path)), 0)

        # Simulates the user input (raw_input)
        quit_command = StringIO.StringIO("q")
        sys.stdin = quit_command

        logobot.main(["-i", self.input_path, "-l", self.logo_path, "-o", self.output_path, "-s", size, "-p", position, "-t", type])
        
        # Wait some seconds until the images are saved
        time.sleep(5)
        
        self.assertEqual(len(os.listdir(self.output_path)), 3)

if __name__ == '__main__':
    unittest.main()

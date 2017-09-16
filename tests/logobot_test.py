import sys
import unittest
import os

sys.path.append('./src')
from logo import Logo
from logobot import LogoBot

class LogoBotTest(unittest.TestCase):
    
    path = os.path.dirname(os.path.abspath(__file__))

    def test_number_of_files(self):
        logo_bot = LogoBot(None)
        self.assertEqual(logo_bot.number_of_files(""), 0)
        self.assertEqual(logo_bot.number_of_files(self.path + "\input"), 3)

    def test_run(self):
        logo = Logo(self.path + "\input", self.path + "\logo.png", self.path + "\output")
        logo_bot = LogoBot(logo)
        
        output_path = self.path + "\output"

        if output_path > 0:
            for dirname, dirnames, filenames in os.walk(output_path):
                for filename in filenames:
                    try:
                        os.remove(filename)
                    except Exception:
                        pass

        self.assertEqual(logo_bot.number_of_files(output_path), 0)

        logo_bot.run()
        self.assertEqual(logo_bot.number_of_files(output_path), 3)

if __name__ == '__main__':
    unittest.main()

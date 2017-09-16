import sys
import unittest

sys.path.append('./src')
from logo import Logo

class LogoTest(unittest.TestCase):
    def test1(self):
        logo = Logo("", "", "")
        logo_bot = LogoBot(logo)
        logo_bot.run()

if __name__ == '__main__':
    unittest.main()

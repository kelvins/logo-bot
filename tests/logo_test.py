import sys
import unittest

sys.path.append('./src')
from logo import Logo

class LogoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

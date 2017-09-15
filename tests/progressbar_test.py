import sys
import unittest

sys.path.append('./src')
from progressbar import ProgressBar

class ProgressBarTest(unittest.TestCase):
    def test_default_values(self):
        pb = ProgressBar(100)
        self.assertEqual(pb.total, 100)
        self.assertEqual(pb.prefix, "Progress:")
        self.assertEqual(pb.suffix, "Complete")
        self.assertEqual(pb.decimals, 2)
        self.assertEqual(pb.bar_length, 50)
        self.assertEqual(pb.char, "#")

    def test_update(self):
        pb = ProgressBar(150, "Progresso:", "Completo", 4, 100, "|")
        
        # Update with different values
        pb.update(50)
        pb.update(-10)
        pb.update(250)
        pb.update(150)

        # Check if the values are correct
        self.assertEqual(pb.total, 150)
        self.assertEqual(pb.prefix, "Progresso:")
        self.assertEqual(pb.suffix, "Completo")
        self.assertEqual(pb.decimals, 4)
        self.assertEqual(pb.bar_length, 100)
        self.assertEqual(pb.char, "|")

if __name__ == '__main__':
    unittest.main()

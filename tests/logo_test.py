
import os
import sys
import unittest

sys.path.append('./src')
from logo import Logo

class LogoTest(unittest.TestCase):

    path = os.path.dirname(os.path.abspath(__file__))

    def test_run(self):
        output_path = self.path + "/../output/"
        logo = Logo(self.path + "/../input/", self.path + "/../logo.png", output_path, 20, "bottom_right", "png")

        for dirname, dirnames, filenames in os.walk(output_path):
            for filename in filenames:
                try:
                    os.remove(dirname+filename)
                except Exception:
                    pass

        self.assertEqual(len(os.listdir(output_path)), 0)

        logo.add()
        self.assertEqual(len(os.listdir(output_path)), 3)

    def test_calc_size(self):
        logo = Logo(self.path + "/../input/", self.path + "/../logo.png", self.path + "/../output/", 50, "bottom_right", "png")

        width, height = logo.calc_size((800, 600), (0, 150))
        self.assertEqual(width, 0)
        self.assertEqual(height, 0)

        width, height = logo.calc_size((100, 100), (100, 100))
        self.assertEqual(width, 50)
        self.assertEqual(height, 50)

        width, height = logo.calc_size((100, 100), (50, 10))
        self.assertEqual(width, 50)
        self.assertEqual(height, 10)

        width, height = logo.calc_size((800, 600), (100, 150))
        self.assertEqual(width, 200)
        self.assertEqual(height, 300)

    def test_calc_position(self):
        logo = Logo(self.path + "/../input/", self.path + "/../logo.png", self.path + "/../output/", 20, "bottom_right", "png")

        logo.position = "center"
        x, y = logo.calc_position((800, 600), (0, 150))
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        image_size = (100, 100)
        logo_size = (50, 50)

        expected_x = [25, 0, 25, 50, 50, 50, 25, 0, 0]
        expected_y = [25, 0, 0, 0, 25, 50, 50, 50, 25]
        position = ["center", "top_left", "top_center", "top_right", "center_right", "bottom_right", "bottom_center", "bottom_left", "center_left"]

        for index in range(x):
            logo.position = position[index]
            x, y = logo.calc_position(image_size, logo_size)
            self.assertEqual(x, expected_x[index])
            self.assertEqual(y, expected_y[index])

if __name__ == '__main__':
    unittest.main()

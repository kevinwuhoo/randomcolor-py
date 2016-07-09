import unittest
import randomcolor
import sys

# these tests have different expected colors for python 2 vs 3 because
# random.randint uses random.choice, which has different implementations
# in python 2 and 3
class TestRandomColor(unittest.TestCase):

    def setUp(self):
        self.rand_color = randomcolor.RandomColor(42)
        self.py_version = sys.version_info[0]

    def test_count(self):
        self.assertEqual(len(self.rand_color.generate()), 1)

        num_to_generate = 10
        colors = self.rand_color.generate(count=num_to_generate)
        self.assertEqual(len(colors), num_to_generate)

    def test_hue(self):
        if self.py_version == 3:
            expected_colors = ['#b98bd3', '#ac5ed1', '#a786d6']
        else:
            expected_colors = ['#dec0f7', '#6d2cd6', '#d5abea']

        purple = self.rand_color.generate(hue='purple', count=3)
        self.assertEqual(purple, expected_colors)

    def test_luminosity(self):
        if self.py_version == 3:
            expected_colors = ['#d35098', '#3dce6e', '#dbf760']
        else:
            expected_colors = ['#5061b7', '#95d319', '#ce56a2']

        bright = self.rand_color.generate(luminosity='bright', count=3)
        self.assertEqual(bright, expected_colors)

    def test_hue_luminosity(self):
        if self.py_version == 3:
            expected_color = ['#b27910']
        else:
            expected_color = ['#bf7a13']

        color = self.rand_color.generate(hue='orange', luminosity='dark')
        self.assertEqual(color, expected_color)

    def test_format(self):
        if self.py_version == 3:
            expected_color_rgb = ['rgb(7, 7, 7)']
            expected_color_hex = ['#4f4f4f']
        else:
            expected_color_rgb = ['rgb(5, 5, 5)']
            expected_color_hex = ['#383838']

        color_rgb = self.rand_color.generate(hue='monochrome', format_='rgb')
        color_hex = self.rand_color.generate(hue='monochrome')

        self.assertEqual(color_rgb, expected_color_rgb)
        self.assertEqual(color_hex, expected_color_hex)

    def test_seed(self):
        if self.py_version == 3:
            expected_color = ['#e094be']
        else:
            expected_color = ['#c0caf7']

        color = self.rand_color.generate()
        self.assertEqual(color, expected_color)
        self.assertEqual(color, randomcolor.RandomColor(42).generate())


if __name__ == '__main__':
    unittest.main()

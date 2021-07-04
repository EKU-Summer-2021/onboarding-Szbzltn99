import unittest
import math
from src.euklides_list import euklides


class EuklidesListTest(unittest.TestCase):
    def euklides_list_test(self):
        x_list_of_points = [1, 2]
        y_list_of_points = [3, 4]
        number = [math.sqrt(
            math.pow((2-1), 2) +
            math.pow((4-3), 2)), math.sqrt(
            math.pow((2-1), 2) +
            math.pow((4-3), 2))]
        expected = number
        actual = euklides(x_list_of_points, y_list_of_points)

        self.assertEqual(expected, actual)

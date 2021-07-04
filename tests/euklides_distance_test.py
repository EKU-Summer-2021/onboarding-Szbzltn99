import unittest
from src.euklides_distance import euklides_distance_matrix
import pandas
import numpy as np


class EuklidesDistanceTest(unittest.TestCase):
    def test_euklides_distance(self):

        data = pandas.DataFrame(np.zeros((1, 1)))
        expected = True
        actual = isinstance(euklides_distance_matrix(data, [1, 2], [3, 4]), pandas.core.frame.DataFrame)
        self.assertEqual(expected, actual)

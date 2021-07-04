import unittest
from src.euklides_distance import euklides_distance_matrix
import pandas
import numpy as np


class CsvReadTest(unittest.TestCase):
    def test_csv_read_test(self):

        data = pandas.DataFrame(np.zeros((1, 1)))
        expected = True
        actual = isinstance(euklides_distance_matrix(data, [1, 2], [3, 4]), pandas.core.frame.DataFrame)
        self.assertEqual(expected, actual)

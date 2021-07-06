import unittest
from src.tsp_class import tsp


class CsvReadTest(unittest.TestCase):
    def test_csv_read_test(self):
        actual = tsp.cost()
        expected = 421.5888978265829

        self.assertEqual(expected, actual)

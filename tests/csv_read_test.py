import unittest
from src.csv_read import csv_read
import pandas


class CsvReadTest(unittest.TestCase):
    def test_csv_read_test(self):

        expected = True
        actual = isinstance(csv_read(
            'https://github.com/EKU-Summer-2021'
            '/intelligent_system_data/blob/main/Intelligent%20System%20Data/TSP/10.csv'
            '?raw=true'), pandas.DataFrame)
        self.assertEqual(expected, actual)

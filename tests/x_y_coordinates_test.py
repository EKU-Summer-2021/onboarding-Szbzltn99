import unittest
from src.x_y_coordinates import x_y_coordinates
from src.csv_read import csv_read


class XYcoordinatesTest(unittest.TestCase):
    def test_x_y_coordinates(self):
        dataframe = csv_read(
            'https://github.com/EKU-Summer-2021/intelligent_system_data'
            '/blob/main/Intelligent%20System%20Data/TSP/10.csv'
            '?raw=true')
        x_coordinates, y_coordinates = x_y_coordinates(dataframe)
        expected = True
        actual = isinstance(x_coordinates, list) and isinstance(y_coordinates, list)
        self.assertEqual(expected, actual)

"""
class to the TSP problem
"""
import math
import pandas as pd
import numpy as np
from src.csv_read import csv_read


class TSP:
    """
    class to the TSP problem
    """
    def __init__(self, url):
        self.data = csv_read(url)
        self.x_points, self.y_points = self.x_y_coordinates()
        self.matrix = self.euclidean_distance()
        self.path = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def x_y_coordinates(self):
        """
        Putting the x and the y coordinates into 2 lists
        """
        x_list_of_points = []
        y_list_of_points = []
        num_rows = len(self.data)
        j = 0
        i = 0
        while j < num_rows:
            if i == 0:
                number = self.data[i][j]
                x_list_of_points.append(number)
                i = 1
            else:
                number = self.data[i][j]
                y_list_of_points.append(number)
                i = 0
                j = j + 1
        return x_list_of_points, y_list_of_points

    def euclidean(self):
        """
        Calculating the euclidean distances and putting them into a list
        """
        eu_list = []
        i = -1
        while i < len(self.x_points) - 1:
            j = 0
            i = i + 1
            while j < len(self.x_points):
                if j == i:
                    j = j + 1
                else:
                    result = math.sqrt(math.pow((self.x_points[j] - self.x_points[i]), 2) +
                                       math.pow((self.y_points[j] - self.y_points[i]), 2))
                    eu_list.append(result)
                    j = j + 1
        return eu_list

    def euclidean_distance(self):
        """
        putting the calculated distances into a matrix from the list
        """
        i = -1
        num_rows = len(self.data)
        data = pd.DataFrame(np.zeros((num_rows, num_rows)))
        result_list = self.euclidean()
        index = 0
        while index < len(result_list):
            while i < num_rows - 1:
                j = 0
                i = i + 1
                while j < num_rows:
                    if j == i:
                        data[j][i] = 0
                        j = j + 1
                    else:
                        data[j][i] = result_list[index]
                        index = index + 1
                        j = j + 1
        return data

    def cost(self, path):
        """
        cost function
        """
        result = 0
        for i in range(len(path)-1):
            result += self.matrix[path[i]][path[i+1]]
        result += self.matrix[path[-1]][path[0]]
        return result

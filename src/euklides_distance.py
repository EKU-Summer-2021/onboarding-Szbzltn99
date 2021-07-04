"""
putting the calculated distances into a matrix from the list
"""
import pandas as pd
import numpy as np
from src.euklides_list import euklides


def euklides_distance_matrix(df, x_list_of_points, y_list_of_points):
    i = -1
    num_rows, num_cols = df.shape
    d = pd.DataFrame(np.zeros((num_rows, num_rows)))
    result_list = euklides(x_list_of_points, y_list_of_points)
    index = 0
    while index < len(result_list):
        while i < num_rows - 1:
            j = 0
            i = i + 1
            while j < num_rows:
                if j == i:
                    d[j][i] = 0
                    j = j + 1
                else:
                    d[j][i] = result_list[index]
                    index = index + 1
                    j = j + 1
    return d

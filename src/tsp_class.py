"""
class to the TSP problem
"""
from src.csv_read import csv_read
from src.x_y_coordinates import x_y_coordinates
from src.euklides_distance import euklides_distance_matrix
from src.cost import cost


class TSP:
    """
    class to the TSP problem
    """
    df = csv_read(
        'https://github.com/EKU-Summer-2021/intelligent_system_data/blob/'
        'main/Intelligent%20System%20Data/TSP/10.csv'
        + '?raw=true')
    x_list_of_points, y_list_of_points = x_y_coordinates(df)
    matrix = euklides_distance_matrix(df, x_list_of_points, y_list_of_points)
    print(matrix)

    cost(matrix, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


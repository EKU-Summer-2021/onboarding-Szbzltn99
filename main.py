import numpy as np

from src import Polynomial
from src.csv_read import csv_read

if __name__ == '__main__':
    coeffs = np.array([1, 0, 0])
    polynom = Polynomial(coeffs)
    print(polynom.evaluate(3))
    print(polynom.roots())
    csv_read(
        'https://github.com/EKU-Summer-2021/intelligent_system_data/blob/main/Intelligent%20System%20Data/TSP/10.csv'
        '?raw=true')

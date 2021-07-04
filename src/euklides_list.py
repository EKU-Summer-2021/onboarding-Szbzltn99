"""
Calculating the euklides distances and putting them into a list
"""
import math


def euklides(x_list_of_points, y_list_of_points):
    eu_list = []
    i = -1
    while i < len(x_list_of_points)-1:
        j = 0
        i = i+1
        while j < len(x_list_of_points):
            if j == i:
                j = j+1
            else:
                result = math.sqrt(math.pow((x_list_of_points[j]-x_list_of_points[i]), 2) +
                                   math.pow((y_list_of_points[j]-y_list_of_points[i]), 2))
                eu_list.append(result)
                j = j+1
    return eu_list

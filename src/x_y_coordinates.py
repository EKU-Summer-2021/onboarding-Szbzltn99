"""
Putting the x and the y coordinates into 2 lists
"""


def x_y_coordinates(df):
    x_list_of_points = []
    y_list_of_points = []
    num_rows, num_cols = df.shape
    j = 0
    i = 0
    while j < num_rows:
        if i == 0:
            number = df[i][j]
            x_list_of_points.append(number)
            i = 1
        else:
            number = df[i][j]
            y_list_of_points.append(number)
            i = 0
            j = j + 1
    return x_list_of_points, y_list_of_points

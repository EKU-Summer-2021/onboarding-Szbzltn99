from src.csv_read import csv_read


class TSP:
    x_list_of_points = []
    y_list_of_points = []
    df = csv_read(
        'https://github.com/EKU-Summer-2021/intelligent_system_data/blob/main/Intelligent%20System%20Data/TSP/10.csv'
        + '?raw=true')
    num_rows, num_cols = df.shape
    for i in range(num_cols):
        for j in range(num_rows):
            if i == 0:
                x_list_of_points.append(df[j][i])
            else:
                y_list_of_points.append(df[j][i])

    print(x_list_of_points, y_list_of_points)

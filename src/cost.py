"""
calculating the cost of a given path
"""


def cost(dataframe, a1, b2, c3, d4, e5, f6, g7, h8, i9, j10):
    result = dataframe[a1-1][b2-1]+dataframe[b2-1][c3-1]+dataframe[c3-1][d4-1] +\
      dataframe[d4-1][e5-1]+dataframe[e5-1][f6-1]+dataframe[f6-1][g7-1] +\
      dataframe[g7-1][h8-1]+dataframe[h8-1][i9-1]+dataframe[i9-1][j10-1]+dataframe[j10-1][a1-1]
    """
    calculating the cost of a given path
    """

    print(result)

"""
calculating the cost of a given path
"""


def cost(dataframe, a, b, c, d, e, f, g, h, i, j):
    s = dataframe[a-1][b-1]+dataframe[b-1][c-1]+dataframe[c-1][d-1] +\
      dataframe[d-1][e-1]+dataframe[e-1][f-1]+dataframe[f-1][g-1] +\
      dataframe[g-1][h-1]+dataframe[h-1][i-1]+dataframe[i-1][j-1]+dataframe[j-1][a-1]
    print(s)

"""
calculating the cost of a given path
"""


# pylint: disable=too-many-arguments


def cost(dataframe, first, second, third, fourth, fifth, sixth, seventh, eight, ninth, tenth):
    """
    csv file to dataframe
    """

    result = \
        dataframe[first - 1][second - 1] + \
        dataframe[second - 1][third - 1] + \
        dataframe[third - 1][fourth - 1] + \
        dataframe[fourth - 1][fifth - 1] + \
        dataframe[fifth - 1][sixth - 1] + \
        dataframe[sixth - 1][seventh - 1] + \
        dataframe[seventh - 1][eight - 1] + \
        dataframe[eight - 1][ninth - 1] + \
        dataframe[ninth - 1][tenth - 1] + \
        dataframe[tenth - 1][first - 1]

    print(result)

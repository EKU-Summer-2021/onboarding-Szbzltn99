"""
csv file to dataframe
"""
import pandas as pd


def csv_read(url):
    """
    reading csv file
    """
    csv_df = pd.read_csv(url, header=None)
    print(csv_df)

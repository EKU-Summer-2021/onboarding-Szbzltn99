def csv_read(url):
    import pandas as pd
    df = pd.read_csv(url, header=None)
    print(df)

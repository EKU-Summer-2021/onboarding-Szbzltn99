def csv_read(url):
    import pandas as pd
    df = pd.read_csv(url, header=None)
    print(df)


csv_read('https://github.com/EKU-Summer-2021/intelligent_system_data/blob/main/Intelligent%20System%20Data/TSP/10.csv?raw=true')



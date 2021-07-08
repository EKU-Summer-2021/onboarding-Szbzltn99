from src.tsp_class import TSP
from src.sa_solver import SAS
if __name__ == '__main__':
    url = 'https://github.com/EKU-Summer-2021/intelligent_system_data/' \
          'blob/main/Intelligent%20System%20Data/TSP/10.csv?raw=true'
    tsp = TSP(url)
    sas = SAS(tsp)
    sas.solve()

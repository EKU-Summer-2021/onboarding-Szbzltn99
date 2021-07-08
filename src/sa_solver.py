import copy
import random
import numpy as np


class SAS:
    def __init__(self, tsp):
        self.tsp = tsp
        self.path = tsp.path
        self.T = 100
        self.alpha = 0.99

    def solve(self):
        random.shuffle(self.path)
        while self.T > 0.01:
            cost = self.tsp.cost(self.path)
            new_path = copy.copy(self.path)
            random_index = random.sample(range(0, 10), 2)
            new_path[random_index[0]], new_path[random_index[1]] = new_path[random_index[1]], new_path[random_index[0]]
            new_cost = self.tsp.cost(new_path)

            cost_difference = new_cost - cost
            prob = np.exp(-cost_difference / self.T)

            if new_cost < cost:
                self.path = new_path
            else:
                num = np.random.uniform()
                if num < prob:
                    self.path = copy.copy(new_path)
            self.T = self.T * self.alpha
        print(cost, self.path)
        return cost, self.path

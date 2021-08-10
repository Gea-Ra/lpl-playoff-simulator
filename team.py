import numpy as np
from matplotlib import pyplot as plt
class Team:
    def __init__(self, name, power_points, index):
        self.name = name
        self.power_points = power_points
        self.index = index
        self.history = np.zeros(4)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def plot_history(self):
        plt.bar([1, 2, 3, 4], self.history)

    def mean_ranking(self):
        return (np.array([1, 2, 3, 4]) @ self.history) / (np.sum(self.history))
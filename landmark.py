import numpy as np


class Landmark:

    def __init__(self, id):
        self.id = id
        self.position = np.array([0], [0])
        self.position_covariance = np.array([0, 0], [0, 0])

    def update(self):
        pass

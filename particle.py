import numpy as np
import landmark


class Particle:

    def __init__(self):
        self.Pose = np.array([0], [0], [0])
        self.landmark = list()

    def sample(self):
        pass

    def update(self):
        pass

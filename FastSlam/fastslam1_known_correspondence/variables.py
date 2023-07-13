import numpy as np

class Landmark:

    def __init__(self, id = -1 , u = np.array([[0], [0]]), cov = np.array([[0, 0], [0, 0]])):
        self.id = id
        self.u = u
        self.cov = cov

class Particle:

    def __init__(self, landmark, pose = np.array([[0],[0],[0]]), weight = 0):
        self.pose = pose
        self.landmark = landmark
        self.weight = weight

    def update_odom(self,odom):
        self.pose = self.pose.astype(np.float64) + odom.astype(np.float64)

    def find_index(self,id):
        found_object = None
        for i in range(len(self.landmark)):
            if self.landmark[i].id == id:
                found_object = i
                break
        return found_object

class Measurement:

    def __init__(self, u = np.array([[0],[0]]), cov = np.array([[0,0],[0,0]])):
        self.u = u
        self.cov = cov
    


    

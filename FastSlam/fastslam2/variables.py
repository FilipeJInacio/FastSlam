import numpy as np
import math

class Robot:

    def __init__(self, pose = np.array([[0],[0],[0]]), cov = np.array([[0,0,0],[0,0,0],[0,0,0]])):
        self.pose = pose
        self.cov = cov

class Particle:

    def __init__(self, pose = np.array([[0],[0],[0]]), weight = 0, landmark = list(), new_pose = np.array([[0],[0],[0]])):
        self.pose = pose
        self.landmark = landmark
        self.weight = weight
        self.new_pose = new_pose

    def add_new_lm(self,threshold):
        self.landmark.append(Landmark(threshold))

    def update_odom(self,odom):
        self.pose = self.pose.astype(np.float64) + odom.astype(np.float64)



class Landmark:

    def __init__(self , weight, u = np.array([[0], [0]]), cov = np.array([[0, 0], [0, 0]]), Hm = np.array([[0, 0], [0, 0]]), Hx = np.array([[0, 0, 0], [0, 0, 0]]), z_predicted = np.array([[0], [0]])):
        self.u = u
        self.cov = cov
        self.weight = weight
        self.Hm = Hm
        self.Hx = Hx
        self.z_predicted = z_predicted

    


class Measurement:

    def __init__(self, u = np.array([[0],[0]]), cov = np.array([[0,0],[0,0]])):
        self.u = u
        self.cov = cov
    
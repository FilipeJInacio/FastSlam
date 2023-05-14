import numpy as np
import particle


class FastSlam1:

    def __init__(self, number_of_particles=100):
        self.number_of_particles = number_of_particles                              # Number of particles
        self.number_of_landmarks = 0                                                # Number of landmarks
        self.particle = np.empty(number_of_particles, dtype=particle.Particle())    # List of particles
        self.robot = particle.Particle()                                            # Robot

    def run_fastslam_iteration(self, measurement, landmark_id, action):

        # As the motion model been updated?
        temp_particles = np.empty(self.number_of_particles, dtype=particle.Particle()) # Temporary list of particles

        for k in range(self.number_of_particles):
            temp_particles[k] = self.particle[k].sample(action)

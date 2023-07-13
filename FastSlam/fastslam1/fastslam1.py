import numpy as np
import variables
import random
import copy

class FastSlam1:

    def __init__(self,grafic,inicial_pose, number_of_particles=100, mode = "Systematic", resample_constant = 0.5, threshold = 0.5):
        self.number_of_particles = number_of_particles                                              # Number of particles
        self.resample_constant = resample_constant                                                  # Resample constant
        self.threshold = threshold                                                                        # Threshold for adding new landmarks        
        self.particle = np.array([variables.Particle(landmark=list(), pose = np.array(inicial_pose)) for _ in range(self.number_of_particles)])
        self.robot = inicial_pose 
        if mode == "Multinomial":
            self.resample_func = FastSlam1.multinomial_resample
        #elif mode == "Residual":
            #indexes = FastSlam1.residual_resample(self.new_particles[:].weight)
        elif mode == "Stratified":
            self.resample_func = FastSlam1.stratified_resample
        elif mode == "Systematic":
            self.resample_func = FastSlam1.systematic_resample


        self.grafic = grafic
        self.points = list() # Graphical usage

    def predict(self,odom): 
        points_x = list()
        points_y = list()
        for k in range(self.number_of_particles): # Loop over all particles
            self.particle[k].update_odom(odom.u)
            self.particle[k].pose = np.transpose(np.random.multivariate_normal(np.transpose(self.particle[k].pose)[0], odom.cov,1))  # Sample
            points_x.append(self.particle[k].pose[0][0]) # Graphical usage
            points_y.append(self.particle[k].pose[1][0]) # Graphical usage
        self.points.append([points_x,points_y])

    def update(self,z):
        z.u[1][0] = FastSlam1.normalizeAngle(z.u[1][0])

        for k in range(self.number_of_particles): # Loop over all particles
            for j in self.particle[k].landmark: # Measure likelihood of each landmark

                delta = np.array([[j.u[0][0]-self.particle[k].pose[0][0]],[j.u[1][0]-self.particle[k].pose[1][0]]])
                r = np.sqrt(delta[0][0]**2+delta[1][0]**2)

                j.z_predicted = np.array([[np.sqrt(delta[0][0]**2+delta[1][0]**2)],[FastSlam1.normalizeAngle(FastSlam1.normalizeAngle(np.arctan2(delta[1][0],delta[0][0]))-self.particle[k].pose[2][0])]])
                j.H = np.array([[delta[0][0]/r,delta[1][0]/r],[-delta[1][0]/(r**2),delta[0][0]/(r**2)]])

                #print(j.H)
                j.Q = j.H.dot(j.cov).dot(j.H.T) + z.cov

                j.weight = np.linalg.det(2*np.pi*j.Q)**(-0.5)*np.exp((-0.5*(z.u-j.z_predicted).T.dot(np.linalg.inv(j.Q)).dot(z.u-j.z_predicted))[0][0])
                #print([z.u[0][0]-j.z_predicted[0][0],z.u[1][0]-j.z_predicted[1][0],j.weight,np.linalg.det(2*np.pi*j.Q)**(-0.5),np.exp((-0.5*(z.u-j.z_predicted).T.dot(np.linalg.inv(j.Q)).dot(z.u-j.z_predicted))[0][0])])
                #print(np.linalg.inv(j.Q))


            # New feature
            self.particle[k].add_new_lm(self.threshold)

            # feature i'm the most near
            nearest_landmark = max(self.particle[k].landmark, key=lambda x: x.weight)
            self.particle[k].weight = nearest_landmark.weight

            if nearest_landmark == self.particle[k].landmark[-1]: # is it new?
                seen = False
                nearest_landmark.u = np.array([[self.particle[k].pose[0][0]+z.u[0][0]*np.cos(z.u[1][0]+self.particle[k].pose[2][0])],[self.particle[k].pose[1][0]+z.u[0][0]*np.sin(z.u[1][0]+self.particle[k].pose[2][0])]])
                H = np.array([[np.cos(self.particle[k].pose[2][0]+z.u[1][0]), -z.u[0][0]*np.sin(self.particle[k].pose[2][0]+z.u[1][0])], [np.sin(self.particle[k].pose[2][0]+z.u[1][0]), z.u[0][0]*np.cos(self.particle[k].pose[2][0]+z.u[1][0])]])
                nearest_landmark.cov = np.linalg.inv(H.dot(z.cov).dot(H.T))

            else:
                self.particle[k].landmark.pop()
                seen = True
                K = nearest_landmark.cov.dot(nearest_landmark.H.T).dot(np.linalg.inv(nearest_landmark.Q))
                nearest_landmark.u = nearest_landmark.u + K.dot(z.u-nearest_landmark.z_predicted)
                nearest_landmark.cov = (np.eye(2)-K.dot(nearest_landmark.H)).dot(nearest_landmark.cov)

            #print([a.weight for a in self.particle[k].landmark])
        if seen:
            weight_sum = sum([entry.weight for entry in self.particle])
            normalized = np.array([entry.weight/weight_sum for entry in self.particle])
            if 1./np.sum(np.square(normalized))>self.resample_constant:
                self.resample(normalized)
            
        self.particle = sorted(self.particle, key=lambda x: x.weight)
        self.robot = sum(obj.pose * obj.weight for obj in self.particle[self.number_of_particles//2:])/sum([entry.weight for entry in self.particle[self.number_of_particles//2:]])
        # Find the element with the highest weight
        #self.robot.pose = max(self.particle, key=lambda x: x.weight).pose
        self.points.append([self.robot[0][0]+z.u[0][0]*np.cos(z.u[1][0]+self.robot[2][0]),self.robot[1][0]+z.u[0][0]*np.sin(z.u[1][0]+self.robot[2][0])])
        #self.grafic.plot_confidence_ellipse([[z.to_cartesian()[0][0]+self.robot.pose[0][0]],[z.to_cartesian()[1][0]+self.robot.pose[1][0]]],z.cov)
        #print("=====================================")
        return

    def resample(self, normalized_weights):
        
        indexes = self.resample_func(normalized_weights)
        new_particles = np.array([variables.Particle() for _ in range(self.number_of_particles)])

        i=0
        for k in indexes:
            new_particles[i] = variables.Particle(self.particle[k].pose,self.particle[k].weight,copy.deepcopy(self.particle[k].landmark))
            i += 1
        
        self.particle = new_particles
        return 

    def multinomial_resample(weights):
        cumulative_sum = np.cumsum(weights)
        cumulative_sum[-1] = 1.  # avoid round-off errors
        return np.searchsorted(cumulative_sum, random(len(weights)))    

        """     def residual_resample(weights):
        N = len(weights)
        indexes = np.zeros(N, 'i')

        # take int(N*w) copies of each weight
        num_copies = (N*np.asarray(weights)).astype(int)
        k = 0
        for i in range(N):
            for _ in range(num_copies[i]): # make n copies
                indexes[k] = i
                k += 1

        # use multinormial resample on the residual to fill up the rest.
        residual = w - num_copies     # get fractional part
        residual /= sum(residual)     # normalize
        cumulative_sum = np.cumsum(residual)
        cumulative_sum[-1] = 1. # ensures sum is exactly one
        indexes[k:N] = np.searchsorted(cumulative_sum, random(N-k))

        return indexes """   

    def stratified_resample(weights):
        N = len(weights)
        # make N subdivisions, chose a random position within each one
        positions = (random(N) + range(N)) / N

        indexes = np.zeros(N, 'i')
        cumulative_sum = np.cumsum(weights)
        i, j = 0, 0
        while i < N:
            if positions[i] < cumulative_sum[j]:
                indexes[i] = j
                i += 1
            else:
                j += 1
        return indexes
    
    def systematic_resample(weights):
        N = len(weights)

        # make N subdivisions, choose positions 
        # with a consistent random offset
        positions = (np.arange(N) + random.random()) / N

        indexes = np.zeros(N, 'i')
        cumulative_sum = np.cumsum(weights)

        i, j = 0, 0
        while i < N:
            if positions[i] < cumulative_sum[j]:
                indexes[i] = j
                i += 1
            else:
                j += 1
        return indexes
    
    def normalizeAngle(angle):

        while angle > np.pi:
            angle -= 2.0 * np.pi

        while angle < -np.pi:
            angle += 2.0 * np.pi

        return angle 
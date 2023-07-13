import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from matplotlib.animation import PillowWriter

class Plot:
    def __init__(self,path,lim = [-10,10,-10,10]):
        self.path = path
        plt.xlim([lim[0],lim[1]])
        plt.ylim([lim[2],lim[3]])

    def make(self,points):
        for i in points:
            plt.scatter(i[0],i[1])
        plt.show()

    def plot_confidence_ellipse(self,u, cov):
        eigenvalues, eigenvectors = np.linalg.eig(cov)
        theta = np.linspace(0,2*np.pi,1000)
        ellipsis = (np.sqrt(eigenvalues[None,:])*eigenvectors) @ [np.sin(theta),np.cos(theta)]
        plt.plot(ellipsis[0,:]+u[0][0],ellipsis[1,:]+u[1][0])



class Animation:
    def __init__(self,path,lim = [-10,10,-10,10] ):
        self.path = path
        self.fig = plt.figure()
        plt.xlim([lim[0],lim[1]])
        plt.ylim([lim[2],lim[3]])
        self.metadata = dict(title='Movie', artist='Matplotlib')
        self.writer = PillowWriter(fps=30, metadata=self.metadata)
    
    def make(self,points):
        with self.writer.saving(self.fig, self.path, 100):
            for i in points:
                plt.scatter(i[0],i[1])
                self.writer.grab_frame()

    def plot_confidence_ellipse(self,u, cov):
        eigenvalues, eigenvectors = np.linalg.eig(cov)
        theta = np.linspace(0,2*np.pi,1000)
        ellipsis = (np.sqrt(eigenvalues[None,:])*eigenvectors) @ [np.sin(theta),np.cos(theta)]
        plt.plot(ellipsis[0,:]+u[0][0],ellipsis[1,:]+u[1][0])
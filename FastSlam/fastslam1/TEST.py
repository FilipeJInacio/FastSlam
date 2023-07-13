import fastslam1
import numpy as np
import utility
import variables
import math
import random

# utility.Plot("plot.gif",[-5,5,-5,5])

fastslam = fastslam1.FastSlam1(utility.Plot("animations/6.gif",[-5,5,-5,5]),np.array([[0],[0],[0]]),100,"Systematic",0.5)


fastslam.points.append([0,0])

fastslam.predict(variables.Measurement(np.array([[1],[0],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[1],[1],[math.pi/4]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[-1],[1],[math.pi/2]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[1],[math.pi/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[0],[1],[-math.pi/4]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[np.sqrt(2)],[math.pi*3/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[-1],[0],[math.pi/2]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[1],[math.pi/2]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[-1],[0],[0]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[np.sqrt(2)],[math.pi*3/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.update(variables.Measurement(np.array([[1],[0]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[0],[-1],[math.pi/2]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[1],[math.pi/2]]),np.array([[0.001,0],[0,0.001]])))

fastslam.update(variables.Measurement(np.array([[np.sqrt(2)],[-math.pi*3/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[0],[-1],[0]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[np.sqrt(2)],[math.pi*3/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[1],[-1],[math.pi/2]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[2],[math.pi/2]]),np.array([[0.001,0],[0,0.001]])))

fastslam.update(variables.Measurement(np.array([[2],[-math.pi/2]]),np.array([[0.001,0],[0,0.001]])))

# second round

fastslam.predict(variables.Measurement(np.array([[1],[0],[0]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[1],[-1],[-math.pi/4]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[-1],[-1],[-math.pi/2]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[1],[-math.pi/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[0],[-1],[math.pi/4]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[np.sqrt(2)],[-math.pi*3/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[-1],[0],[-math.pi/2]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[1],[-math.pi/2]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[-1],[0],[0]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[np.sqrt(2)],[-math.pi*3/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.update(variables.Measurement(np.array([[1],[0]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[0],[1],[-math.pi/2]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[1],[-math.pi/2]]),np.array([[0.001,0],[0,0.001]])))

fastslam.update(variables.Measurement(np.array([[np.sqrt(2)],[math.pi*3/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[0],[1],[0]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[np.sqrt(2)],[-math.pi*3/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[1],[1],[-math.pi/2]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.update(variables.Measurement(np.array([[2],[-math.pi/2]]),np.array([[0.001,0],[0,0.001]])))

fastslam.update(variables.Measurement(np.array([[2],[math.pi/2]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(variables.Measurement(np.array([[1],[0],[0]]),np.array([[0.001,0,0],[0,0.001,0],[0,0,0.001]])))

fastslam.grafic.make(fastslam.points)



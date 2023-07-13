import fastslam2
import numpy as np
import utility
import variables

# utility.Plot("plot.gif",[-5,5,-5,5])

fastslam = fastslam2.FastSlam2(utility.Plot("animations/6.gif",[-5,5,-5,5]),np.array([[0],[0],[0]]),100,"Systematic",0.5,0.05)


fastslam.points.append([0,0])

fastslam.run(variables.Measurement(np.array([[0],[0],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[1],[np.pi/2]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[1],[0],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[np.sqrt(2)],[np.pi*3/4]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[0],[1],[np.pi/2]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[1],[np.pi/2]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[0],[1],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[np.sqrt(2)],[np.pi*3/4]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[-1],[0],[np.pi/2]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[1],[np.pi/2]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[-1],[0],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[np.sqrt(2)],[np.pi*3/4]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[0],[-1],[np.pi/2]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[1],[np.pi/2]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[0],[-1],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[np.sqrt(2)],[np.pi*3/4]]),np.array([[0.01,0],[0,0.01]])))



fastslam.run(variables.Measurement(np.array([[1],[0],[np.pi/2]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[1],[-np.pi/2]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[1],[0],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[np.sqrt(2)],[-np.pi*3/4]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[0],[-1],[-np.pi/2]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[1],[-np.pi/2]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[0],[-1],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[np.sqrt(2)],[-np.pi*3/4]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[-1],[0],[-np.pi/2]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[1],[-np.pi/2]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[-1],[0],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[np.sqrt(2)],[-np.pi*3/4]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[0],[1],[-np.pi/2]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[1],[-np.pi/2]]),np.array([[0.01,0],[0,0.01]])))

fastslam.run(variables.Measurement(np.array([[0],[1],[0]]),np.array([[0.01,0,0],[0,0.01,0],[0,0,0.001]])),variables.Measurement(np.array([[np.sqrt(2)],[-np.pi*3/4]]),np.array([[0.01,0],[0,0.01]])))


fastslam.grafic.make(fastslam.points)
exit()



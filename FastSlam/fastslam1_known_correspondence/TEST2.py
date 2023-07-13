import fastslam1
import numpy as np
import utility
import variables
import math
import random
import time

# utility.Plot("plot.gif",[-5,5,-5,5])

#start_time = time.perf_counter()
#end_time = time.perf_counter()
#execution_time = end_time - start_time
#sprint(f"The execution time is: {execution_time}")

fastslam = fastslam1.FastSlam1(utility.Plot("animations/plot.gif", [-5, 5, -5, 5]),variables.Robot(np.array([[-3],[0],[np.pi/4]]),np.array([[0.05,0,0],[0,0.05,0],[0,0,0.08]])), 100, "Systematic", 0.5)


# Time 0
fastslam.predict(np.array([[0], [0], [0]]))

# Time 1 Moves to (1,0)
fastslam.predict(np.array([[1], [0], [0]]))

# Time 2 Moves to (1,1)
fastslam.predict(np.array([[1], [1], [0]]))

# Time 3 Moves to (-1,1)
fastslam.predict(np.array([[-1], [1], [0]]))

# Time 3
fastslam.update(1, variables.Measurement(np.array([[1], [math.pi]]), np.array([[0.01, 0], [0, 0.01]])))

# Time 4 Moves to (0,1)
fastslam.predict(np.array([[0], [1], [0]]))

# Time 4
fastslam.update(1, variables.Measurement(np.array([[math.sqrt(2)], [math.pi*5/4]]), np.array([[0.01, 0], [0, 0.01]])))

# Time 5 Moves to (-1,0)
fastslam.predict(np.array([[-1], [0], [0]]))

# Time 5
fastslam.update(1, variables.Measurement(np.array([[1], [math.pi*3/2]]), np.array([[0.01, 0], [0, 0.01]])))

# Time 6 Moves to (-1,0)
fastslam.predict(np.array([[-1], [0], [0]]))

# Time 6
fastslam.update(1, variables.Measurement(np.array([[math.sqrt(2)], [math.pi*7/4]]), np.array([[0.01, 0], [0, 0.01]])))

# Time 6
fastslam.update(2, variables.Measurement(np.array([[1], [math.pi]]), np.array([[0.01, 0], [0, 0.01]])))

# Time 7 Moves to (0,-1)
fastslam.predict(np.array([[0], [-1], [0]]))

# Time 7
fastslam.update(1, variables.Measurement(np.array([[1], [0]]), np.array([[0.01, 0], [0, 0.01]])))

# Time 7
fastslam.update(2, variables.Measurement(np.array([[math.sqrt(2)], [math.pi*3/4]]), np.array([[0.01, 0], [0, 0.01]])))

# Time 8 Moves to (0,-1)
fastslam.predict(np.array([[0], [-1], [0]]))

# Time 8
fastslam.update(1, variables.Measurement(np.array([[math.sqrt(2)], [math.pi/4]]), np.array([[0.01, 0], [0, 0.01]])))

# Time 8
fastslam.update(2, variables.Measurement(np.array([[math.sqrt(3)], [math.pi*16/23]]), np.array([[0.01, 0], [0, 0.01]])))

# Time 9 Moves to (0,-1)
fastslam.predict(np.array([[1], [-1], [0]]))

# Time 9
fastslam.update(1, variables.Measurement(np.array([[2], [math.pi/2]]), np.array([[0.01, 0], [0, 0.01]])))

fastslam.grafic.make(fastslam.points)
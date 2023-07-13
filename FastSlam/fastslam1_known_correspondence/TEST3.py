import fastslam1
import numpy as np
import utility
import variables
import math

# utility.Plot("plot.gif",[-5,5,-5,5])

fastslam = fastslam1.FastSlam1(utility.Plot("animations/1.gif" ,[-5,5,-5,5]),variables.Robot(np.array([[-3],[0],[np.pi/4]]),np.array([[0.05,0,0],[0,0.05,0],[0,0,0.08]])),100,"Systematic",0.5)

fastslam.points.append([fastslam.robot.pose[0][0],fastslam.robot.pose[1][0]])

fastslam.predict(np.array([[0.5],[0.5],[0]]))
fastslam.update(3,variables.Measurement(np.array([[np.sqrt(4.5)],[0]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0.5],[-np.pi/4]]))
fastslam.update(3,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(3.25)],[np.arctan2(1,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.grafic.make(fastslam.points)
exit()

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(1.25)],[np.arctan2(1,0.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(3.25)],[np.arctan2(1,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(10)],[np.arctan2(1,3)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(10)],[-np.arctan2(1,3)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(1.25)],[np.arctan2(1,0.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(7.25)],[np.arctan2(1,2.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(7.25)],[-np.arctan2(1,2.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(5)],[-np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[-0.5],[-np.pi/4]]))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(8,variables.Measurement(np.array([[np.sqrt(8.5)],[np.pi/4-np.arctan2(2.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[-0.5],[-np.pi/4]]))
fastslam.update(8,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(9,variables.Measurement(np.array([[np.sqrt(5)],[-np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[-0.5],[-np.pi/4]]))
fastslam.update(9,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(4.5)],[0]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[-0.5],[-np.pi/4]]))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(3.25)],[np.pi/2-np.arctan2(1.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(3.25)],[np.pi/2-np.arctan2(1.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(10)],[np.pi/2-np.arctan2(3,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(10)],[-np.pi/2+np.arctan2(3,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(7.25)],[np.pi/2-np.arctan2(2.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(7.25)],[-np.pi/2+np.arctan2(2.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(5)],[-np.pi/2+np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0.5],[-np.pi/4]]))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(1,variables.Measurement(np.array([[np.sqrt(8.5)],[np.pi/4-np.arctan2(2.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(2,variables.Measurement(np.array([[np.sqrt(6.5)],[-np.pi/4-np.arctan2(0.5,2.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0.5],[-np.pi/4]]))
fastslam.update(1,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(2,variables.Measurement(np.array([[np.sqrt(5)],[-np.pi/2+np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

# first round
print(fastslam.robot.pose)

fastslam.predict(np.array([[0.5],[0.5],[-np.pi/4]]))
fastslam.update(3,variables.Measurement(np.array([[np.sqrt(4.5)],[0]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0.5],[-np.pi/4]]))
fastslam.update(3,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(3.25)],[np.arctan2(1,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(1.25)],[np.arctan2(1,0.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(3.25)],[np.arctan2(1,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(10)],[np.arctan2(1,3)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(10)],[-np.arctan2(1,3)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(1.25)],[np.arctan2(1,0.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(7.25)],[np.arctan2(1,2.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(7.25)],[-np.arctan2(1,2.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(5)],[-np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[-0.5],[-np.pi/4]]))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(8,variables.Measurement(np.array([[np.sqrt(8.5)],[np.pi/4-np.arctan2(2.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[-0.5],[-np.pi/4]]))
fastslam.update(8,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(9,variables.Measurement(np.array([[np.sqrt(5)],[-np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[-0.5],[-np.pi/4]]))
fastslam.update(9,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(4.5)],[0]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[-0.5],[-np.pi/4]]))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(3.25)],[np.pi/2-np.arctan2(1.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(3.25)],[np.pi/2-np.arctan2(1.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(10)],[np.pi/2-np.arctan2(3,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(10)],[-np.pi/2+np.arctan2(3,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(7.25)],[np.pi/2-np.arctan2(2.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(7.25)],[-np.pi/2+np.arctan2(2.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(5)],[-np.pi/2+np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0.5],[-np.pi/4]]))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(1,variables.Measurement(np.array([[np.sqrt(8.5)],[np.pi/4-np.arctan2(2.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(2,variables.Measurement(np.array([[np.sqrt(6.5)],[-np.pi/4-np.arctan2(0.5,2.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0.5],[-np.pi/4]]))
fastslam.update(1,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(2,variables.Measurement(np.array([[np.sqrt(5)],[-np.pi/2+np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

# second round
print(fastslam.robot.pose)

fastslam.predict(np.array([[0.5],[0.5],[0]]))
fastslam.update(3,variables.Measurement(np.array([[np.sqrt(4.5)],[0]]),np.array([[0.001,0],[0,0.001]])))

print(fastslam.robot.pose)

fastslam.predict(np.array([[0.5],[0.5],[-np.pi/4]]))
fastslam.update(3,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(3.25)],[np.arctan2(1,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(1.25)],[np.arctan2(1,0.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(3.25)],[np.arctan2(1,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(10)],[np.arctan2(1,3)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(10)],[-np.arctan2(1,3)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(1.25)],[np.arctan2(1,0.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(7.25)],[np.arctan2(1,2.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(7.25)],[-np.arctan2(1,2.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(5)],[-np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[-0.5],[-np.pi/4]]))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(8,variables.Measurement(np.array([[np.sqrt(8.5)],[np.pi/4-np.arctan2(2.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[-0.5],[-np.pi/4]]))
fastslam.update(8,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(9,variables.Measurement(np.array([[np.sqrt(5)],[-np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[-0.5],[-np.pi/4]]))
fastslam.update(9,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(4.5)],[0]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[-0.5],[-np.pi/4]]))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(3.25)],[np.pi/2-np.arctan2(1.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(3.25)],[np.pi/2-np.arctan2(1.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(10)],[np.pi/2-np.arctan2(3,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(10)],[-np.pi/2+np.arctan2(3,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(7.25)],[np.pi/2-np.arctan2(2.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(7.25)],[-np.pi/2+np.arctan2(2.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(5)],[-np.pi/2+np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0.5],[-np.pi/4]]))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(1,variables.Measurement(np.array([[np.sqrt(8.5)],[np.pi/4-np.arctan2(2.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(2,variables.Measurement(np.array([[np.sqrt(6.5)],[-np.pi/4-np.arctan2(0.5,2.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0.5],[-np.pi/4]]))
fastslam.update(1,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(2,variables.Measurement(np.array([[np.sqrt(5)],[-np.pi/2+np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

# third loop

fastslam.predict(np.array([[0.5],[0.5],[-np.pi/4]]))
fastslam.update(3,variables.Measurement(np.array([[np.sqrt(4.5)],[0]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0.5],[-np.pi/4]]))
fastslam.update(3,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(3.25)],[np.arctan2(1,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(4,variables.Measurement(np.array([[np.sqrt(1.25)],[np.arctan2(1,0.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(3.25)],[np.arctan2(1,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(10)],[np.arctan2(1,3)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(10)],[-np.arctan2(1,3)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(5,variables.Measurement(np.array([[np.sqrt(1.25)],[np.arctan2(1,0.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(7.25)],[np.arctan2(1,2.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(7.25)],[-np.arctan2(1,2.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[0],[0]]))
fastslam.update(6,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(5)],[-np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[-0.5],[-np.pi/4]]))
fastslam.update(7,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(8,variables.Measurement(np.array([[np.sqrt(8.5)],[np.pi/4-np.arctan2(2.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[0.5],[-0.5],[-np.pi/4]]))
fastslam.update(8,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(9,variables.Measurement(np.array([[np.sqrt(5)],[-np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[-0.5],[-np.pi/4]]))
fastslam.update(9,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(4.5)],[0]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[-0.5],[-np.pi/4]]))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(10,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(3.25)],[np.pi/2-np.arctan2(1.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(11,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(3.25)],[np.pi/2-np.arctan2(1.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(2)],[np.pi/4]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(10)],[np.pi/2-np.arctan2(3,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(10)],[-np.pi/2+np.arctan2(3,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(12,variables.Measurement(np.array([[np.sqrt(1.25)],[np.pi/2-np.arctan2(0.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(7.25)],[np.pi/2-np.arctan2(2.5,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(7.25)],[-np.pi/2+np.arctan2(2.5,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0],[0]]))
fastslam.update(13,variables.Measurement(np.array([[np.sqrt(5)],[np.pi/2-np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(5)],[-np.pi/2+np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0.5],[-np.pi/4]]))
fastslam.update(14,variables.Measurement(np.array([[np.sqrt(2.5)],[np.pi/4-np.arctan2(0.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(1,variables.Measurement(np.array([[np.sqrt(8.5)],[np.pi/4-np.arctan2(2.5,1.5)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(2,variables.Measurement(np.array([[np.sqrt(6.5)],[-np.pi/4-np.arctan2(0.5,2.5)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.predict(np.array([[-0.5],[0.5],[-np.pi/4]]))
fastslam.update(1,variables.Measurement(np.array([[np.sqrt(5)],[np.arctan2(1,2)]]),np.array([[0.001,0],[0,0.001]])))
fastslam.update(2,variables.Measurement(np.array([[np.sqrt(5)],[-np.pi/2+np.arctan2(2,1)]]),np.array([[0.001,0],[0,0.001]])))

fastslam.grafic.make(fastslam.points)

exit()



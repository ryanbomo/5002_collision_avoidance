import math, re
import Collision_avoidance.py as Collision_avoidance

class Aircraft:
  neighbors = {}
  
  def __init__(self, myInfo):
    self.ID = myInfo[0]
    self.x = myInfo[1]
    self.y = myInfo[2]
    self.z = myInfo[3]
    self.speed = myInfo[4]
    self.cardinality = myInfo[5]
    
  def listen(self):
    return thing
  
  def broadcast(self):
    return thing
  
  def check_neighbors(self):
    myInfo = [self.ID, self.x, self.y, self.z]
    invInfo = [2,9500,9500,9500]
    caInstance = Collision_avoidance(invInfo,myInfo)
    didAdjust = caInstance.run_ca()
    if (didAdjust>0):
        self.y = caInstance.myY


airplaneInfo = [1,10000,10000,10000,200,40]
print(myairplane.y)
myairplane = Aircraft(airplaneInfo)
myairplane.check_neighbors()
print(myairplane.y)

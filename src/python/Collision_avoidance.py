import math, re

class Collision_avoidance:
  MINDIST = 1000
  
  def __init__(self, invInfo, myInfo):
    invInfo[0] = self.invID
    invInfo[1] = self.invX
    invInfo[2] = self.invY
    invInfo[3] = self.invZ
    myInfo[0] = self.myID
    myInfo[1] = self.myX
    myInfo[2] = self.myY
    myInfo[3] = self.myZ
    
  def run_ca(self):
    ##figure goUp
    if (myY < invY):
        goUp = 0
    elif (myY > invY):
        goUp = 1
    else:
        if (myID > invID):
            goUp = 1
        else:
            goUp = 0
        
    
    ## calc distance
    xSqr = (self.myX - self.invX) * (self.myX - self.invX)
    ySqr = (self.myY - self.invY) * (self.myY - self.invY)
    zSqr = (self.myZ - self.invZ) * (self.myZ - self.invZ)
    mySqr = xSqr + ySqr + zSqr
    myDistance = math.sqrt(mySqr)
    if (myDistance < MINDIST):
      self.calc_adujst(myDistance,goUp)
      return 1
    else:
      return 0
    
  def calc_adjust(self,distance,goUp):
    adjustDistance = distance/2
    if (goUp =0):
      self.myY = self.myY -adjustDistance
    elif (goUp=1):
      self.myY = self.myY + adjustDistance


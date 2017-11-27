import math, re

class Collision_avoidance:
    MINDIST = 1000


    ## Collision avoidance initialization variables
    def __init__(self, invInfo, myInfo):
        self.invID = invInfo[0]
        self.invX = invInfo[1]
        self.invY = invInfo[2]
        self.invZ = invInfo[3]
        self.myID = myInfo[0]
        self.myX = myInfo[1]
        self.myY = myInfo[2]
        self.myZ = myInfo[3]

    ## 
    def run_ca(self):
        ##figure goUp
        if (self.myY < self.invY):
            goUp = 0
        elif (self.myY > self.invY):
            goUp = 1
        else:
            if (self.myID > self.invID):
                goUp = 1
            else:
                goUp = 0
        
    
        ## calc distance
        xSqr = (self.myX - self.invX) * (self.myX - self.invX)
        ySqr = (self.myY - self.invY) * (self.myY - self.invY)
        zSqr = (self.myZ - self.invZ) * (self.myZ - self.invZ)
        mySqr = xSqr + ySqr + zSqr
        myDistance = math.sqrt(mySqr)
        if (myDistance < self.MINDIST):
            print("Intruder is " + str(myDistance) + " units away")
            self.calc_adjust(myDistance,goUp)
            return 1
        else:
            return 0
    
    def calc_adjust(self,distance,goUp):
        adjustDistance = distance/2
        if (goUp == 0):
            self.myY = self.myY -adjustDistance
        elif (goUp==1):
            self.myY = self.myY + adjustDistance

            
class Aircraft:
    neighbors = {}

    ## These are the variable that it initializes with
    def __init__(self, myInfo):
        self.ID = myInfo[0]
        self.x = myInfo[1]
        self.y = myInfo[2]
        self.z = myInfo[3]
        self.speed = myInfo[4]
        self.cardinality = myInfo[5]

    ## This is a sort of input
    def listen(self):
        return thing

    ## This is a sort of output
    def broadcast(self):
        return thing
  
    def check_neighbors(self):
        ## set up info for CA
        myInfo = [self.ID, self.x, self.y, self.z]
        invInfo = [2,9500,9500,9500]
        
        ## create the collision avoidance object and call it
        caInstance = Collision_avoidance(invInfo,myInfo)
        didAdjust = caInstance.run_ca()
        if (didAdjust>0):
            self.y = caInstance.myY


airplaneInfo = [1,10000,10000,10000,200,40]
myairplane = Aircraft(airplaneInfo)
print("My current height is " + str(myairplane.y))
myairplane.check_neighbors()
print("My new height will be " + str(myairplane.y))

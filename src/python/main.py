## Correct speed so that it is a property of the plane, and so that steps work correctly
## Fix Move() function

import math, re, sqlite3

##
conn = sqlite3.connect('airwaves.db')
c=conn.cursor()

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

    
    def run_ca(self):
        ##figure goUp
        if (self.myY < self.invY):
            goUp = 0
        elif (self.myY > self.invY):
            goUp = 1
        elif (self.myID > self.invID):
            goUp = 1
        elif (self.myID < self.invID):
            goUp = 0
        return goUp
        
    
        ## calc distance
        xSqr = (self.myX - self.invX) * (self.myX - self.invX)
        ySqr = (self.myY - self.invY) * (self.myY - self.invY)
        zSqr = (self.myZ - self.invZ) * (self.myZ - self.invZ)
        mySqr = xSqr + ySqr + zSqr
        myDistance = math.sqrt(mySqr)
        if (myDistance < self.MINDIST):
            print(str(self.myID) + ":Intruder Detected.")
            print(str(self.myID) + ":Intruder is " + str(myDistance) + " units away.")
            print(str(self.myID) + ":Evasive Action Needed.")
            self.calc_adjust(myDistance,goUp)
            return 1
        else:
            return 0
    
    def calc_adjust(self,distance,goUp):
        adjustDistance = (self.MINDIST-distance)/2
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
        print(str(self.ID)+": Listening.")
        self.neighbors = db_reader(self.ID)

    ## This is a sort of output
    def broadcast(self):
        print(str(self.ID)+": Broadcasting.")
        infoList = [self.ID, self.x, self.y, self.z, self.speed, self.cardinality]
        db_writer(infoList)


    ##
    def check_neighbors(self):
        print(str(self.ID)+": Checking Neighbors.")
        myInfo = [self.ID, self.x, self.y, self.z]
        ## print(myInfo)
        for i in self.neighbors:
            invInfo = [i]
            for j in self.neighbors[i]:
                invInfo.append(j)
            ## create the collision avoidance object and call it
            caInstance = Collision_avoidance(invInfo,myInfo)
            didAdjust = caInstance.run_ca()
            if (didAdjust>0):
                self.y = caInstance.myY
        

    ## NEEDS WORK, NOT CORRECT VERSION, JUST FOR CLASS DEMO NOW
    ## NOT WORKING CORRECTLY in DEMO VERSION EITHER
    def move(self):
        print(str(self.ID)+": Moving.")
        if self.cardinality == 0:
            self.z = self.z + self.speed
        if self.cardinality == 180:
            self.z = self.z -self.speed
##        if 0<=(self.cardinality)<90 or 270<(self.cardinality)<=360:
##            x_sign = 1
##        elif 90<(self.cardinality)<270:
##            x_sign = -1
##        else:
##            x_sign = 0
##        if
        

## NEED TO UPDATE PER CLASS DISCUSSION
class Simulator:
    indef = False
    airplanes = []
    
    def __init__(self, stepNum):
        self.steps = stepNum

    def createAirplanes(self):
        sqliteGet = "SELECT * FROM airwaves;"
        for row in c.execute(sqliteGet):
            planeInfo = [row[0],row[1],row[2],row[3],row[4],row[5]]
            self.airplanes.append(Aircraft(planeInfo))
            
    def run_sim(self):
        simStep = 0
        if self.steps ==0:
            self.indef = True
        if self.indef:
            while self.indef:
                print("This is step: " +str(simStep))
                for a in self.airplanes:
                    a.listen()
                    a.check_neighbors()
                    a.move()
                    a.broadcast()
                commit_stage()
                simStep +=1
        else:
            while simStep < self.steps:
                simStep+=1
                print("This is step: " +str(simStep))
                for a in self.airplanes:
                    a.listen()
                    a.check_neighbors()
                    a.move()
                    a.broadcast()
                
                
## commits stage changes
def commit_stage():
    sqliteUpdate = '''UPDATE airwaves
SET
      x = (SELECT stage.x 
                            FROM stage
                            WHERE stage.airplane_id = airwaves.airplane_id )
    , y = (SELECT stage.y
                            FROM stage
                            WHERE stage.airplane_id = airwaves.airplane_id )
    , z = (SELECT stage.z
                            FROM stage
                            WHERE stage.airplane_id = airwaves.airplane_id )
WHERE
    EXISTS (
        SELECT *
        FROM stage
        WHERE stage.airplane_id = airwaves.airplane_id
    )'''
    c.execute(sqliteUpdate)
    conn.commit()
    return 1


## This writes to the database, currently platform specific
def db_writer(infoList):
    sqliteUpdate = "UPDATE stage SET x=" + str(infoList[1]) + ",y=" + str(infoList[2]) + ",z=" + str(infoList[3]) +" WHERE airplane_id = " + str(infoList[0])+";"
    c.execute(sqliteUpdate)
    conn.commit()
    return 1

## This reads from the database, currently platform specific
def db_reader(ID):
    neighborDict = {}
    sqliteGet = "SELECT * FROM airwaves WHERE airplane_id !="+str(ID)+";"
    for row in c.execute(sqliteGet):
        dataSet = [row[1],row[2],row[3],row[4],row[5]]
        dictID = row[0]
        neighborDict[dictID] = dataSet
    return neighborDict



            

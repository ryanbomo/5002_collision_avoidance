## Correct speed so that it is a property of the plane, and so that steps work correctly
## Fix Move() function

import math, sqlite3

##
conn = sqlite3.connect('airwaves.db')
c=conn.cursor()

class Collision_avoidance:
    MINDIST = 1000

    def update_ca(self, myInfo, invInfo):
        self.invID = invInfo[0]
        self.invX = invInfo[1]
        self.invY = invInfo[2]
        self.invZ = invInfo[3]
        self.myID = myInfo[0]
        self.myX = myInfo[1]
        self.myY = myInfo[2]
        self.myZ = myInfo[3]

    
    def run_ca(self):        ## calc distance
        xSqr = (self.myX - self.invX) * (self.myX - self.invX)
        ySqr = (self.myY - self.invY) * (self.myY - self.invY)
        zSqr = (self.myZ - self.invZ) * (self.myZ - self.invZ)
        mySqr = xSqr + ySqr + zSqr
        myDistance = math.sqrt(mySqr)
        if (myDistance < self.MINDIST):
            print(str(self.myID) + ": Intruder Detected.")
            print(str(self.myID) + ": Intruder is " + str(myDistance) + " units away.")
        ##figure goUp
            if (self.myY < self.invY):
                print(str(self.myID) + ": Evasive Action Needed - Go Down!")
                goUp = 0
            elif (self.myY > self.invY):
                print(str(self.myID) + ": Evasive Action Needed - Go Up!")
                goUp = 1
            elif (self.myID > self.invID):
                print(str(self.myID) + ": Evasive Action Needed - Go Up!")
                goUp = 1
            elif (self.myID < self.invID):
                print(str(self.myID) + ": Evasive Action Needed - Go Down!")
                goUp = 0
        else:
            goUp = -1
        return goUp

    
 
        
class Mover:
    ANGLE_ASCENT = 5
    ANGLE_DESCENT = 5

    def __init__(self, my_speed, my_id):
        self.speed = my_speed
        self.myID = my_id

    def move(self, goUp, my_x, my_y, my_z, card):
        if (goUp == 1):
            ## calc ascent
            ascent = math.sin((self.ANGLE_ASCENT*math.pi)/180)*self.speed
            newY = my_y + ascent
            ## calc vertical movement
            vert = math.cos((self.ANGLE_ASCENT*math.pi)/180)*self.speed
            newXZ = self.vert_move(my_x, my_z, vert, card)
            print(str(self.myID) + ": Moving Up to " + str(newXZ[0])+ ", " + str(newY) + ", " + str(newXZ[1]))
            ## return new coords
        elif (goUp == 0):
            ## calc descent
            descent = math.sin((self.ANGLE_DESCENT*math.pi)/180)*self.speed
            newY = my_y - descent
            ## calc verticla movment
            vert = math.cos((self.ANGLE_DESCENT*math.pi)/180)*self.speed
            newXZ = self.vert_move(my_x, my_z, vert, card)
            print(str(self.myID) + ": Moving Down to " + str(newXZ[0])+ ", " + str(newY) + ", " + str(newXZ[1]))
        else:
            newY = my_y
            newXZ = self.vert_move(my_x, my_z, self.speed, card)
            print(str(self.myID) + ": Moving Flat to " + str(newXZ[0])+ ", " + str(newY) + ", " + str(newXZ[1]))
            
            
        newCoords = [newXZ[0], newY, newXZ[1]]
        return newCoords
    
    def vert_move(self, x, z, dist, card):
        x_change = math.sin((card*math.pi)/180)*dist
        ## floating point issues
        if (abs(x_change) < (0.17*dist)):
            x_change = 0
        z_change = math.cos((card*math.pi)/180)*dist
        if (abs(z_change) < (0.17*dist)):
            z_change = 0
        new_x = x + x_change
        new_z = z + z_change
        return [new_x, new_z]
        

class Communicator:

    def __init__(self, myID):
        self.ID = myID

    def listen(self, ID):
        neighbors = db_reader(self.ID)
        return neighbors
        
        
    def broadcast(self, x, y, z, speed, cardinality):
        infoList = [self.ID, x, y, z, speed, cardinality]
        db_writer(infoList)

        
        
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
        self.caInstance = Collision_avoidance()
        self.mover = Mover(self.speed, self.ID)
        self.communicator = Communicator(self.ID)
        
    def listen(self):
        ## Listen for Neighbors
        self.neighbors = self.communicator.listen(self.ID)

    def broadcast(self):
        ## Broadcast Move
        self.communicator.broadcast(self.x, self.y, self.z, self.speed, self.cardinality)

    def move(self):
        ## Move
        newcoords = self.mover.move(self.goUp, self.x, self.y, self.z, self.cardinality)
        self.x = newcoords[0]
        self.y = newcoords[1]
        self.z = newcoords[2]

        
    def collision_avoidance(self):
        myInfo = [self.ID, self.x, self.y, self.z]
        ## print(myInfo)
        if not self.neighbors:
            didAdjust = -1
        for i in self.neighbors:
            invInfo = [i]
            for j in self.neighbors[i]:
                invInfo.append(j)
            ## create the collision avoidance object and call it
            self.caInstance.update_ca(myInfo, invInfo)
            didAdjust = self.caInstance.run_ca()
        self.goUp = didAdjust
        
        


class Simulator:
    
    def __init__(self, stepNum, steps_per_second):
        self.steps = stepNum
        self.sps = steps_per_second
        self.airplanes = []

    def create_airplanes(self):
        sqliteGet = "SELECT * FROM airwaves;"
        for row in c.execute(sqliteGet):
            print(row)
            planeInfo = [row[0],row[1],row[2],row[3],(row[4]/self.sps),row[5]]
            self.airplanes.append(Aircraft(planeInfo))
            
    def run_sim(self):
        simStep = 0
        if self.steps ==0:
            while True:
                simStep +=1
                print("This is step: " +str(simStep))
                for a in self.airplanes:
                    a.listen()
                    a.collision_avoidance()
                    a.move()
                    a.broadcast()
                commit_stage()
        else:
            while simStep < self.steps:
                simStep+=1
                print("This is step: " +str(simStep))
                for a in self.airplanes:
                    a.listen()
                    a.collision_avoidance()
                    a.move()
                    a.broadcast()
                commit_stage()
                
                
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



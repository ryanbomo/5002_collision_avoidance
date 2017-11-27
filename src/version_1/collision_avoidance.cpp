#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <math.h>

#include "collision_avoidance.h"

#define MINDIST 8000


void Collision_avoidance::Collision_avoidance(triCoords *myCurCoords,int myFlightNum)
{
    myCoordinates = malloc(sizeof(*myCoordinates));
    myCoordinates->x = myCurCoords.x;
    myCoordinates->y = myCurCoords.y;
    myCoordinates->y = myCurCoords.z;
    myFlightID = myFlightNum;
    
}


// check to see if we need to avoid stuff
int Collision_avoidance::compute_ca(triCoords invCurCoords, int invFlightID)
{
  int myX, myY, myZ, invX, invY, invZ, myID, invID, goUp;
  myX = myCoordinates.x;
  myY = myCoordinates.y;
  myZ = myCoordinates.z;
  invX = invCurCoords.x;
  invY = invCurCoords.y;
  invZ = invCurCoords.z;
  myID = myFlightID;
  invID = invFlightID;
  
  if (myY>invY){
    goUp = 1;
  }else if (myY<invY){
    goUp = 0;
  }else {
    if (myID > invID){
      goUp = 1;
    }else if (myID < invID){
      goUp = 0;
    }
  }
  
  float xSqr = (myX - invX) * (myX - invX);
  float ySqr = (myY - invY) * (myY - invY);
  float zSqr = (myZ - invZ) * (myZ - invZ);

  double mySqr = xSqr + ySqr + zSqr;

  double myDistance = sqrt(mySqr);
  if (abs(myDistance) > MINDIST){
    return 0;
  } else if (abs(myDistance)<=MINDIST){
    calc_adjust(myDistance/2, goUp);
    return 1;
  }
}


// adjust collision course based on height only
void Collision_avoidance::calc_adjust(int dist, int goUp)
{
  int newY, adjustBy;
  adjsutBy = MINDIST-dist;
  adjustBy = adjustBy/2;
  if (goUp = 0){
    while(newY-adjustBy <= 1000){
      adjustBy = adjustBy/2;
      if (adjustBy <1) {
        adjusBy = 0;
      }
    }
    newY = myCoordinates.y-adjustBy;
    myCoordinates.y = newY;
  }else if (goUp = 1){
    newY = myCoordinates.y+adjustBy;
    myCoordinates.y = newY;
  }
}

triCoords Collision_avoidance::get_my_coords()
{
    return myCoordinates;
}



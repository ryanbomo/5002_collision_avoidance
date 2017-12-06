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


int Collision_avoidance::compute_ca(triCoords invCurCoords, int invFlightID)
{
  int myX, myY, myZ, invX, invY, invZ, myID, invID, upDown;
  myX = myCoordinates.x;
  myY = myCoordinates.y;
  myZ = myCoordinates.z;
  invX = invCurCoords.x;
  invY = invCurCoords.y;
  invZ = invCurCoords.z;
  myID = myFlightID;
  invID = invFlightID;
  
  if (myY>invY){
    upDown = 1;
  }else if (myY<invY){
    upDown = 0;
  }else {
    if (myID > invID){
      upDown = 1;
    }else if (myID < invID){
      upDown = 0;
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
    calc_adjust(myDistance/2, upDown);
    return 1;
  }
}

void Collision_avoidance::calc_adjust(int dist, int upDown)
{
  if (upDown = 0){
   // adjust down 
  }else if (upDown = 1){
   // adjust up 
  }
}

triCoords Collision_avoidance::get_my_coords()
{
    return myCoordinates;
}



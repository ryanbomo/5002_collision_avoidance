#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <math.h>

#include "collision_avoidance.h"

#define MINDIST 8000


void Collision_avoidance::Collision_avoidance(int myFlightNum, int x, int y, int z)
{

    myFlightID = myFlightNum;
    myX = x;
    myY = y;
    myZ = z;
    
}


// check to see if we need to avoid stuff
int Collision_avoidance::compute_ca(int invFlightNum, int x, int y, int z)
{
  int invX, invY, invZ, myID, invID, goUp;
  invX = x;
  invY = y;
  invZ = z;
  invID = invFlightNum;
  
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
  adjustBy = MINDIST-dist;
  adjustBy = adjustBy/2;
  if (goUp = 0){
    while(newY-adjustBy <= 1000){
      adjustBy = adjustBy/2;
      if (adjustBy <1) {
        adjustBy = 0;
      }
    }
    newY = myY-adjustBy;
    myY = newY;
  }else if (goUp = 1){
    newY = myY+adjustBy;
    myY = newY;
  }
}

int Collision_avoidance::get_myX()
{
    return myX;
}

int Collision_avoidance::get_myY()
{
    return myY;
}

int Collision_avoidance::get_myZ()
{
    return myZ;
}



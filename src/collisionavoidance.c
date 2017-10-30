#include "collisionavoidance.h"
const int  minDist = 1000;

int collisionAvoidance(int ownAlt, int invAlt, int distance, int myflightNum, int invflightNum){
  int adjustAltBy;
  if (distance<minDist){
    adjustAltBy = (minDist-distance)/2;
    if (ownAlt < invAlt){
      adjustAltBy = (avoid)*-1;
    }else if(ownAlt = invAlt){
      if (myflightNum < invflightNum){
      adjustAltBy = (avoid)*-1;
	
    }
    
  }else{
    adjustAltBy = 0;
  }
  return adjustAltBy;
}


/*
 * This will be a draft of a better x,y,z coordinate collision avoidance system



int betterCollisionAvoidance(triCoords mycoords, triCoords invCoords, int distance){
  
}

*/
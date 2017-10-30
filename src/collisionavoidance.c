#include "collisionavoidance.h"
const int  minDist = 1000;

int collisionAvoidance(int ownAlt, int invAlt, int distance){
  int avoid;
  if (distance<minDist){
    avoid = (minDist-distance)/2;
    if (ownAlt < invAlt){
      avoid = (avoid)*-1;
    }
    
  }else{
    avoid = 0;
  }
  return avoid;
}


/*
 * This will be a draft of a better x,y,z coordinate collision avoidance system



int betterCollisionAvoidance(triCoords mycoords, triCoords invCoords, int distance){
  
}

*/
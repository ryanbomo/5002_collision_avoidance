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

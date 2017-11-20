// collision_avoidance.h
#ifndef collision_avoidance_H
#define collision_avoidance_H

struct triCoords {
  int x;
  int y;
  int z;
};

class Collision_avoidance{
  private:
    struct triCoords myCoordinates;
    int myFlightID;
  public:
    //functions
    void Collision_avoidance(triCoords myCurCoords,int myFlightID);
    int compute_ca(triCoords invCurCoords, int invFlightID);
    triCoords calc_adjust(int dist, int upDown);
    triCoords get_my_coords();
};

#endif
// collision_avoidance.h
#ifndef collision_avoidance_H
#define collision_avoidance_H

class Collision_avoidance{
  private:
    int myX, myY, myZ; //airplanes X, Y, Z coordinates
    int myFlightID;
  public:
    //functions
    void Collision_avoidance(int myFlightNum, int X, int Y, int Z);
    int compute_ca(int invX, int invY, int invZ, int invFlightID);
    int calc_adjust(int dist, int upDown);
    int get_myX();
    int get_myY();
    int get_myZ();
};

#endif
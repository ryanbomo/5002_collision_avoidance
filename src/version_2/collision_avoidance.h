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
		triCoords myCoordinates;
		triCoords invCoordinates;
		int myFlightID;
		int invFlightID;
	public:
		//functions
		void update_info(triCoords myCurCoords, triCoords invCurCoords, int myFlightID, int invFlightID); 
		int compute_ca();
		triCoords return_adjust();
}

#endif
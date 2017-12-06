// aircraft.h
#ifndef aircraft_H
#define aircraft_H

struct triCoords {
  int x;
  int y;
  int z;
};

class Aircraft{
	private:
		int speed;		//aircraft speed
        int cardinality; //0-359 to represent direction
		triCoords my_coords;	//tri coordinate structre of my coordinates
		Collision_avoidance CA;	//declaration of collision avoidance object
		int AircraftReg;	//unique alpha numeric identifier
		bool aircraftNearby;	//bool value for seeing if aircraft nearby
		Aircraft *neighbors[];	//array of neighbors
	public:
		//functions
		void Aircraft(int inSpeed, triCoords initTriCoords, int flightNum);			//set up initialize
		string broadcast();		//send data
		string check_neighbors();	//check for neighbors
		string listen();		//grab neighbors broadcast
};

#endif
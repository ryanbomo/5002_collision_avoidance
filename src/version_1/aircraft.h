// aircraft.h
#ifndef aircraft_H
#define aircraft_H


class Aircraft{
	private:
		int speed;		//aircraft speed
		int myX, myY, myZ;	// aircraft x,y and z coori
		Collision_avoidance CA;	//declaration of collision avoidance object
		int AircraftID;		//unique numeric identifier
		bool aircraftNearby;	//bool value for seeing if aircraft nearby
		Aircraft *neighbors[];	//array of neighbors
	public:
		//functions
		void Aircraft(int inSpeed, int myX, int myY, int myZ, int flightNum);			//set up initialize
		string broadcast();		//send data
		string check_neighbors();	//check for neighbors
		string listen();		//grab neighbors broadcast
};

#endif
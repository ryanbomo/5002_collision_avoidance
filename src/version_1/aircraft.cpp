#include <string.h>

#include "aircraft.h"

string Aircraft::broadcast()
{
    //broadcast my current tri_coords
    //go to column on CSV where top box = aircraft ID
      // second box = myCoordiantes.x;
      // third box = myCoordinates.y;
      // fourth box = myCoordinates.z;
      // fifth box = speed;
      // sixth box = cardinality;
}

string Aircraft::check_neighbors()
{
  int numNeighbors, numChecks;
  Collision_avoidance* ca = new Collision_avoidance(*myCoordinates, AircraftID);

    // get numNeighbors

  numChecks = numNeighbors;
  while (numChecks >0){
    //For Each Neighbor
    for (int i=0;i<numNeighbors;i++){
      ca.compute_ca();
    }
        //Check CA against neighbor's triCoords
        //if Adjust:
            //Adjust
        //Else
            //do not adjust

  numChecks = numChecks - 1;
  }
}

int Aircraft::listen()
{
    //grab neighbors broadcast info
    // if aircraft nearby, update bool
        //add aircraft to dictionary ifnot already in dictionary
            //dictionary format is {flightID:triCoords}

}

void Aircraft::init(int inSpeed, triCoords initTriCoords, int flightNum)
{
    //initialize all the stuff the aircraft does
    // should have:
        //speed
        //my tri_coordinates
        //flight_ID

}

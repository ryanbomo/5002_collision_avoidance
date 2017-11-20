#include <string.h>

#include "aircraft.h"

string Aircraft::broadcast()
{
    //broadcast my current tri_coords
}

string Aircraft::check_neighbors()
{
    //for each Neighbor and until not moves are made:
        //Check CA against neighbors triCoords
        //if Adjust:
            //Adjust
        //Else
            //do not adjust
       //IF move was made, run loop again to find correct adjustments
}

string Aircraft::listen()
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

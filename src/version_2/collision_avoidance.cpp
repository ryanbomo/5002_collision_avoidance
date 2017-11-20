#include <string.h>

#include "collision_avoidance.h"

int Collision_avoidance::compute_ca()
{
    //checks distance using tricoord system
    //IF too close:
        //run calc_adjust()
        //return 1
    //else
        //return 0
}

void Collision_avoidance::calc_adjust()
{
    //looks at current distance and desired distance for amount to adjust by
    // if lower
        //adjust by that much down
    //else if higher
        //adjust by that much up
    // else if same
        //use flightID to tell if up or down
}

void Collision_avoidance::update_tri_coords(triCoords myCurCoords, triCoords invCurCoords, int myFlightID, int invFlightID)
{
   //code stuff goes here
}
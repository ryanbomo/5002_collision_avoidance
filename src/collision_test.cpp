#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <ctype.h>
#include <unistd.h>
#include "collisionavoidance.h"

int main(int argc,char *argv[]){
  int ownAlt,invAlt,distance;
  while ((option = getopt(argc, argv, "m::i::d::")) != -1) {
    switch (option) {
      case 'm':
	ownAlt = atoi(optarg);
	break;
      case 'i':
	invAlt = atoi(optarg);
	break;
      case 'd':
	distance = atoi(optarg);
	break;
      default: 
	cerr << "Usage: CollisionSim [-f <fileName>]" << endl;
	cerr << "   -f <CSV_Name>           Assigns filename of Simulation Info" << endl;
	exit(EXIT_FAILURE);
    }
  }
  
  int adjust = collisionAvoidance(ownAlt,invAlt,distance);
  fprintf(stderr,"Adjust is %u\n", adjust);
  
}
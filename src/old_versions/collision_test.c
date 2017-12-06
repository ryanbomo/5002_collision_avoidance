#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <unistd.h>
#include "collisionavoidance.h"

int main(int argc,char *argv[]){
  int ownAlt,invAlt,distance, flightnum, invflightnum;
  int option, cerr;
  
  opterr = 0;
  while ((option = getopt(argc, argv, "m::i::d::n::I::")) != -1) {
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
      case 'n':
	flightnum = atoi(optarg);
	break;
      case 'I':
	invflightnum = atoi(optarg);
	break;
      default: 
        abort ();
    }
  }
  
  fprintf(stderr,"My alt is %d\n", ownAlt);
  fprintf(stderr,"Invader alt is %d\n", invAlt);
  fprintf(stderr,"Distance is %d\n", distance);
  fprintf(stderr,"My flight number is %d\n", flightnum);
  fprintf(stderr,"Their flight number is %d\n", invflightnum);
  
  int adjust = collisionAvoidance(ownAlt,invAlt,distance,flightnum, invflightnum );
  fprintf(stderr,"Adjust is %d\n", adjust);
  
}
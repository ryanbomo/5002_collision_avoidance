#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <unistd.h>
#include "collisionavoidance.h"

int main(int argc,char *argv[]){
  int ownAlt,invAlt,distance;
  int option, cerr;
  
  opterr = 0;
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
        abort ();
    }
  }
  
  fprintf(stderr,"My alt is %d\n", ownAlt);
  fprintf(stderr,"Invader alt is %d\n", invAlt);
  fprintf(stderr,"Distance is %d\n", distance);
  
  int adjust = collisionAvoidance(ownAlt,invAlt,distance);
  fprintf(stderr,"Adjust is %d\n", adjust);
  
}
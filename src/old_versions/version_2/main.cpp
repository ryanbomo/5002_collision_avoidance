#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include "aircraft.h"
#include "collision_avoidance.h"




int main(int argc,char *argv[]){

	string strcmd1;
        int option;
	int simTime;

	while ((option = getopt(argc, argv, "f::t:")) != -1) {
		switch (option) {
		case 'f':
			strcmd1 = optarg;
			break;
		case 't':
			simTime = atoi(optarg);
		default: 
		    cerr << "Usage: CollisionSim [-f <fileName>]" << endl;
		    cerr << "   -f <CSV_Name>           Assigns filename of Simulation Info" << endl;
		    exit(EXIT_FAILURE);
		}
	}
	string file_name = strcmd1;
	// process file, should take in CSV and give an array of Aircraft
	file_processor(strcmd1);
	// Run Simulator for set amount of time, if no time is set, run indefinitely
	run_sim(simTime)
  
}

void file_processor(strcmd1){
	//for each aircraft in .CSV, create new aircraft

}

void run_sim(simTime){
	if (simTime>0){
		while (simTime>0){
			//for each aircraft
				sim_step();
			simTime = simTime - 1;
		}
	} else {
		while(true){
			//for each aircraft
				sim_step();
		}
	}
}

void sim_step(){
			//listen
		//set step
		//take step

}

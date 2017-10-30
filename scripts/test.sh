#!/bin/bash
cd ../
cd ./src/
SCRIPT=$(readlink -f "$0")
./main -m"10000" -i"10100" -d"985" -n"1003" -I"1100"